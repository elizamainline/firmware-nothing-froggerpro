#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
"""Wrap FroggerPro's stock WLAN board data and regdb for ath11k API 2."""

import struct
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME = b"bus=ahb,qmi-chip-id=1,qmi-board-id=255,variant=Nothing_FroggerPro"
OUTPUT = ROOT / "lib/firmware/updates/ath11k/WCN6750/hw1.0/board-2.bin"


def tlv(kind, data):
    return struct.pack("<II", kind, len(data)) + data + bytes(-len(data) % 4)


def main():
    image = b"QCA-ATH11K-BOARD\0".ljust(20, b"\0")
    for kind, filename in enumerate(("bdwlan.bin", "regdb.bin")):
        data = (ROOT / "lib/firmware/qca6750" / filename).read_bytes()
        if not data:
            raise ValueError(f"{filename} is empty")
        image += tlv(kind, tlv(0, NAME) + tlv(1, data))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(image)
    print(f"{OUTPUT.relative_to(ROOT)}: {len(image)} bytes")


if __name__ == "__main__":
    main()
