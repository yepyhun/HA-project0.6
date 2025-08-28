# utils/driver_factory.py
import os, logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import undetected_chromedriver as uc

log = logging.getLogger(__name__)

def make_driver():
    mode = os.getenv("STEALTH_MODE", "selenium").strip().lower()
    headless = os.getenv("HEADLESS", "1") == "1"
    profile_path = os.getenv("CHROME_PROFILE_PATH", "").strip()
    chrome_major_env = os.getenv("CHROME_MAJOR", "").strip()

    if mode == "uc":
        opts = uc.ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
        if profile_path:
            opts.add_argument(f"--user-data-dir={profile_path}")
        if chrome_major_env.isdigit():
            driver = uc.Chrome(options=opts, version_main=int(chrome_major_env))
        else:
            driver = uc.Chrome(options=opts)
        log.info("driver=uc headless=%s chrome_major=%s", headless, chrome_major_env or "auto")
        return driver

    # baseline: Selenium
    opts = ChromeOptions()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=opts)
    log.info("driver=selenium headless=%s", headless)
    return driver
