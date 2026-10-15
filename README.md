# Nothing Phone (4a) Pro firmware

Firmware for the Nothing Phone (4a) Pro (FroggerPro, A069P, Qualcomm SM7750).
The files were extracted from a European retail device running
`Nothing/FroggerProEEA/FroggerPro:16/BQ2A.250913.001-BP2A.250605.031.A3/2607231820:user/release-keys`.

The `lib/firmware` tree contains firmware loaded by Linux drivers. Qualcomm
PIL images were combined from the stock `.mdt` and `.bXX` files using
[`pil-squasher`](https://github.com/andersson/pil-squasher). The
`usr/share/qcom` tree contains the stock audio calibration, DSP libraries and
sensor configuration used by Qualcomm userspace.

Personal calibration and identifiers from `/mnt/vendor/persist` are not
included. The radio bootloader partition images are also outside this runtime
firmware collection.

The ath11k board file under `lib/firmware/updates` wraps the unmodified
`qca6750/bdwlan.bin` and `qca6750/regdb.bin` in the driver's API 2 format.
Regenerate it with `python3 tools/make-ath11k-board.py`. It requires
`qcom,ath11k-calibration-variant = "Nothing_FroggerPro"` in the Wi-Fi device
tree node. The variant distinguishes this phone from the generic WCN6750
reference board, which has the same chip ID 1 and board ID 255. Using the
generic board data allows 2.4 GHz connections but causes 5 GHz authentication
frames to complete without acknowledgements on the tested phone.

The `updates` directory takes precedence over distribution firmware without
overwriting the `linux-firmware` package's board file. This override is specific
to FroggerPro; the corresponding variant entries can eventually be included
in the shared upstream `board-2.bin` instead.

The files are proprietary and retain their owners' licenses. No license to
redistribute or modify them is granted by this repository.
