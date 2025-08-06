### 📚 Table of Contents

* [Dataset Description](#dataset-description)
* [Dataset Parts](#dataset-parts)
* [Data Structure and File Organization](#data-structure-and-file-organization)
* [Downloads](#downloads)
* [Examples and Teasers](#examples-and-teasers)
* [Acknowledgement](#acknowledgement)

# The Viking Hill Dataset and Technical Details

## Dataset description
![Viking hill in Orebro](media/viking_hill_sm.jpg)
*The recorded track captures the [Enbuskabacken](https://www.lansstyrelsen.se/orebro/besoksmal/kulturmiljoer/enbuskabacken.html) area in Örebro.*

This dataset is one of the competition tracks in the SLAM challenge organized by the [Resilient SLAM in Challenging Settings](https://comrob.github.io/ecmr25slam/#about) workshop at the [ECMR 2025](https://ecmr2025.dei.unipd.it/).
The dataset consists of a single long trajectory through a forested area (approx. 200x200m) at the Örebro university campus.
It was recorded in summer 2024, during the vegetation peak. The terrain is uneven because the area used to serve as a burial ground during the Viking Age (550-1050 AD).
The dataset includes LiDAR, 4D Radar, GNSS, RGB camera and IMU.

---

## Dataset Parts
### Public Training Part

* **grass_track_training** (1566s)
 Initial portion of the area (the northern part)

### Hidden Testing Part

* **grass_track_test** (3813s)
 The complete area, including the southern part.  
---

## Data Structure and File Organization

```
grass_track_training/
├── calibration
│   ├── extrinsics
│   │   ├── extrinsics.txt
│   │   └── frames.pdf
│   └── intrinsics
│       ├── camera_calibration.txt
│       └── hugin_radar_startup_params.txt
├── LICENSE.txt
├── readme.txt
├── reference
│   ├── reference.txt
│   └── supplementary
│       ├── reference_train_bagfile.bag
│       ├── reference_train_gps_rtk_in_robot_time.csv
│       └── source_rtk_solution_from_Emlid_RTKLIB
│           ├── gps_filtered_high_accuracy.pos
│           ├── gsp_original_post_fix_including_bad_sections.pos
│           └── train_robot_time_to_gps_time.csv
├── sensors
│   ├── grass_track_training__2025-06-12-22-12-48_0.bag
│   ├── ...
│   └── grass_track_training__2025-06-12-23-38-13_31.bag
└── tracks
    └── default.txt
```

* `grass_track_training__<sequence time and number>.bag` → Raw sensory data and static transforms.
* `reference/` → Folder containing reference RTK trajectories.
* `calibration/extrinsics/` → Transformations between sensor frames.
* `calibration/instrinsics/` → Intrinsic parameters for the camera and radar settings.

### Sensors
The dataset provides sensor measurements from these sensors:

* Sensrad Hugin A3-Sample (solid-state 4D radar)
  * Please note that the Hugin A3-Sample radar used in our dataset is an early demo model not with the same performance as the forthcoming production-ready model.
* Ouster OS0-32 (3D lidar)
  * This sensor is available for tuning and verification of your SLAM solution, but not available in the competition runs (i.e., the topic with point clouds will not be published in the Docker environment).  
* IDS Imaging uEye camera (2056x1542px)
* Xsens MTi-30 (IMU)
* Emlid Reach RS2+ (RTK-GNSS receiver pair)

### Reference Contents

The dataset contains a `reference/` subdirectory with:

* `reference_train_bagfile.bag`: Reference GNSS RTK localization synchrized with the robot time, saved as a bag file.
* `reference.txt`: The GNSS RTK expressed in the UTM coordinates, with time stamps from the robot. Format: **timestamp[s], northing[m], easting[m], elevation, qx, qy, qz, qw**. Note that the quarternion is always identity.
* `reference_train_gps_rtk_in_robot_time.csv`: Contains the same information as `reference.txt`, but expressed in latitude and longitude. Format: **secs, nsecs, latitude, longitude, elevation**.
* `gps_filtered_high_accuracy.pos`: RTK solution used to generate the reference samples for the files above. It does not contain sections with too few sattelites. Note that the displayed time is the GPS time (no time zone, no step seconds).
* `gsp_original_post_fix_including_bad_sections.pos`: Complete RTK solution, wih all samples including the noisy ones.
* `train_robot_time_to_gps_time.csv`: Conversion from the robot time to the time indicated by the GNSS. The robot was no exactly synchronized with the GNSS, there is approx. 0.6s offset. This file can be used to match those times. Format: **robot secs, robot nsecs, gnss secs, gnss nsecs** 

---

## Downloads

* [All training data](https://cloud.oru.se/s/6jFmgbrsq7Amrde) (32 GB in total)

---

## Examples and Teasers

![Viking hill in Orebro](media/husky_sm.jpg)

*Recorded in June, the grass was tall enough to often obscure the robot sensors.*

![Viking hill in Orebro](media/vegetation_sm.jpg)

*The robot was intentionally driven through bushes and over uneven terrain.*

### Video Teasers

[![Watch the video](https://img.youtube.com/vi/WGpa2mYYAf0/default.jpg)](https://youtu.be/WGpa2mYYAf0)
[![Watch the video](https://img.youtube.com/vi/Ioj59OIlEVM/default.jpg)](https://youtu.be/Ioj59OIlEVM)

## Acknowledgement

The work on this dataset was supported by the European Union's Horizon Europe Framework Programme under the RaCOON project (ID: 101106906).

![Funded by EU](media/EN_FundedbytheEU_RGB_POS.png)


