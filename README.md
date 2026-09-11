# 📷 Kavro API Suite

> **UAT API Test Framework for the KAVRO Camera Device (NB166 CameraPod)**  
> Built with Python + Pytest | REST API Automation | Designed for UAT Standards

---

## 📁 Project Structure

```
Kavro_API_Suite/
│
├── api/
│   └── get_api.py          # DeviceAPI class — all HTTP method wrappers
│
├── config/
│   └── config.py           # Device IP, credentials (BASE_URL, USERNAME, PASSWORD)
│
├── data/
│   └── data.json           # Test data — payloads, expected values, configs
│
├── tests/
│   ├── test_get.py                 # Device info — GET /device/info
│   ├── test_device_status.py       # Device status — uptime, CPU, memory, temp
│   ├── test_device_control.py      # Factory reset & reboot
│   ├── test_log.py                 # Device logs — get & clear
│   ├── test_http.py                # HTTP/HTTPS mode — get & post
│   ├── test_network.py             # Network IPv4/IPv6 — get & post
│   ├── test_onvif.py               # ONVIF mode — get & post
│   ├── test_rtsp.py                # RTSP/RTSPS mode — get & post
│   ├── test_rtp.py                 # RTP sessions — get & terminate
│   ├── test_webui.py               # Web UI mode — get & post
│   ├── test_rstp.py                # RSTP config — get & post
│   ├── test_time.py                # System time & time settings — get & post
│   ├── test_certificate.py         # SSL Certificates — get, generate, restore
│   ├── test_video.py               # Video common & streams — get & post
│   ├── test_image.py               # Image settings, ROI, overlay, frame
│   ├── test_motion.py              # Motion detection — config, events, status
│   ├── test_video_clips.py         # Video clips — generate, status, download
│   ├── test_sdcard.py              # SD card — status, usage, mount/unmount/format
│   ├── test_firmware.py            # Firmware — version, update, update status
│   └── test_user.py                # User management — add, update, delete, password
│
├── reports/                # HTML & Allure test reports (auto-generated)
├── conftest.py             # Pytest fixtures — session, auth, data loader
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## ⚙️ Configuration

Edit `config/config.py` to point to your device:

```python
BASE_URL = "https://<device-ip>/api/v1"
USERNAME = "apc"
PASSWORD = "your_password"
```

> SSL verification is disabled by default for local device testing.

---

## 🧪 Test Data

All test payloads and expected values are stored in `data/data.json`.

| Key | Description |
|---|---|
| `get_info` | Device info expected values |
| `get_status` | Device status expected values |
| `system_control` | Factory reset & reboot payloads |
| `rtp_sessions` | RTP session list & terminate ID |
| `webui_mode` | Web UI enable/disable payloads |
| `rstp_config` | RSTP enable/disable payloads |
| `system_time` | Clock values for time tests |
| `time_settings` | NTP / manual time config |
| `certificates` | Certificate generate payload |
| `video_common` | Frame rate settings |
| `video_streams` | Stream list & specific stream config |
| `image_settings` | Brightness, contrast, WB, flip, etc. |
| `roi_exposure` | ROI coordinates |
| `overlay_settings` | Timestamp overlay position |
| `motion_config` | Motion sensitivity, mask, expected status |
| `video_clips` | Clip generate payload & clip ID |
| `sd_card` | SD card status & usage values |
| `firmware` | Firmware version & update status |
| `network_ipv4` | IPv4 DHCP / Static configs |
| `onvif_mode` | ONVIF enable/disable |
| `rtsp_mode` | RTSP / RTSPS mode |
| `add_usr` | User add/update payloads |
| `delete_usr` | User delete payload |
| `pwd_change` | Password change payload |
| `http_mode` | HTTP/HTTPS enable configs |

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run All Tests

```bash
pytest tests/
```

### 3. Run a Specific Test File

```bash
pytest tests/test_video.py
pytest tests/test_image.py
```

### 4. Run by Marker

```bash
pytest -m smoke        # smoke tests
pytest -m pwd          # password change tests
pytest -m log          # log tests
```

### 5. Run with Verbose Output

```bash
pytest tests/ -v
```

### 6. Generate HTML Report

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### 7. Generate Allure Report

```bash
pytest tests/ --alluredir=reports/allure_results
allure serve reports/allure_results
```

---

## 🏗️ Framework Design

### `conftest.py` — Fixtures

| Fixture | Description |
|---|---|
| `apiclient` | Returns `(session, base_url)` — session with auth & SSL bypass |
| `device_data` | Loads and returns `data/data.json` as a Python dict |

### `api/get_api.py` — `DeviceAPI` Class

All API calls are abstracted into methods on the `DeviceAPI` class. Tests instantiate it using the `apiclient` fixture:

```python
session, base_url = apiclient
client = DeviceAPI(session, base_url)
response = client.get_video_streams("/video/streams")
```

---

## 📊 Test Coverage Summary

| Module | Test File | Tests |
|---|---|---|
| Device Info | `test_get.py` | 6 |
| Device Status | `test_device_status.py` | 1 |
| Device Control | `test_device_control.py` | 2 |
| Logs | `test_log.py` | 2 |
| HTTP Mode | `test_http.py` | 2 |
| Network IPv4/IPv6 | `test_network.py` | 3 |
| ONVIF | `test_onvif.py` | 2 |
| RTSP / RTSPS | `test_rtsp.py` | 2 |
| RTP Sessions | `test_rtp.py` | 2 |
| Web UI | `test_webui.py` | 2 |
| RSTP | `test_rstp.py` | 2 |
| System Time | `test_time.py` | 4 |
| Certificates | `test_certificate.py` | 4 |
| Video Streams | `test_video.py` | 5 |
| Image Settings | `test_image.py` | 8 |
| Motion Detection | `test_motion.py` | 5 |
| Video Clips | `test_video_clips.py` | 3 |
| SD Card | `test_sdcard.py` | 6 |
| Firmware | `test_firmware.py` | 3 |
| User Management | `test_user.py` | 4 |
| **Total** | **20 files** | **69 tests** |

---

## 📦 Key Dependencies

| Package | Purpose |
|---|---|
| `pytest` | Test runner |
| `requests` | HTTP client for API calls |
| `pytest-html` | HTML test reports |
| `allure-pytest` | Allure report integration |
| `pytest-xdist` | Parallel test execution |
| `pytest-rerunfailures` | Auto-retry on flaky tests |
| `urllib3` | SSL warning suppression |

---

## 📝 Notes

- This framework is designed for **UAT (User Acceptance Testing)** of the KAVRO NB166 CameraPod REST API.
- All tests follow a **minimal, readable pattern** — no complex abstractions — for easy maintenance and confidence.
- Test data is fully **data-driven** via `data.json` — update values there without touching test logic.
- SSL is disabled (`session.verify = False`) since devices use self-signed certificates in local environments.
