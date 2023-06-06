# Reads the USB VID and PID from the file specified by sys.argv[1] and then
# inserts those values into the template file specified by sys.argv[2],
# printing the result to stdout

from __future__ import print_function

import sys
import re
import string

config_prefix = "MICROPY_HW_USB_"
needed_keys = ("USB_PID_CDC_MSC", "USB_PID_CDC_HID", "USB_PID_CDC", "USB_VID")


def parse_usb_ids(filename):
    rv = {}
    for line in open(filename):
        line = line.rstrip("\r\n")
        match = re.match("^#define\s+(\w+)\s+\(0x([0-9A-Fa-f]+)\)$", line)
        if match and match[1].startswith(config_prefix):
            key = match[1].replace(config_prefix, "USB_")
            val = match[2]
            # print("key =", key, "val =", val)
            if key in needed_keys:
                rv[key] = val
    for k in needed_keys:
        if k not in rv:
            raise Exception(f"Unable to parse {k} from {filename}")
    return rv


if __name__ == "__main__":
    usb_ids_file = sys.argv[1]
    template_file = sys.argv[2]
    replacements = parse_usb_ids(usb_ids_file)
    for line in open(template_file, "r"):
        print(string.Template(line).safe_substitute(replacements), end="")
