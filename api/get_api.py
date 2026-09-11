# api/get_api.py
import requests

class DeviceAPI:  # <--- Make sure the class is named exactly 'DeviceAPI'
    def __init__(self, session, base_url):
        # We pass the session and base URL from the conftest fixture
        self.session = session
        self.base_url = base_url

    def get_req(self, endpoint):
        # Use the session to make the request
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def get_device(self,endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)
    
    def get_logs(self,endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)
    def post_logs(self,endpoint,payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url,json=payload)
    
    def post_user(self,endpoint,payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url,json=payload)

    def get_http(self,endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)
    def post_http(self,endpoint,payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url,json=payload)

    def get_ipv4(self,endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)
    def post_ipv4(self,endpoint,payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url,json=payload)
    def get_onvif(self,endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)
    def post_onvif(self,endpoint,payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url,json=payload)
    def rtsp_mode(self,endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)
    def post_rtsp_mode(self,endpoint,payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url,json=payload)

    # Device & System Control
    def post_factory_reset(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def post_reboot(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    # RTP Sessions
    def get_rtp_sessions(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_terminate_rtp_session(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    # Web UI
    def get_webui(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_webui(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    # RSTP
    def get_rstp(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_rstp(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    # System Time & Time Settings
    def get_time_clock(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_time_clock(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def get_time_settings(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_time_settings(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    # Certificates
    def get_certificate(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def get_certificate_pem(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_certificate(self, endpoint, files=None, data=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, files=files, data=data)

    def post_generate_certificate(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def post_restore_default_certificate(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    # Video Settings & Streams
    def get_video_common(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_video_common(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def get_video_streams(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def get_specific_video_stream(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_specific_video_stream(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    # Image Settings, Frame, ROI, Overlay
    def get_image_settings(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_image_settings(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def post_restore_image_defaults(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def get_roi_exposure(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_roi_exposure(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def get_image_frame(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def get_overlay(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_overlay(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    # Motion Detection
    def get_motion_config(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_motion_config(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def get_motion_events(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_clear_motion_events(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def get_motion_status(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    # Video Clips
    def post_generate_video_clip(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def get_clip_status(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def get_download_video_clip(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    # SD Card Storage
    def get_sd_status(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def get_sd_usage(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_sd_format(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def post_sd_recover(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def post_sd_mount(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    def post_sd_unmount(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)

    # Firmware Management
    def get_firmware_version(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)

    def post_firmware_upload(self, endpoint, files=None, data=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, files=files, data=data)

    def post_firmware_update(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)
    
    def post_firmware_image(self, endpoint, file_path):
        url = f"{self.base_url}{endpoint}"

        with open(file_path, "rb") as firmware:

            response = self.session.post(
            url,
            data=firmware,
            headers={
                "Content-Type": "application/octet-stream"
            },
            verify=False
        )

        return response
    def get_firmware_update_status(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)



      