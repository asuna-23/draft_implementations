import os
from datetime import datetime
from playwright.sync_api import sync_playwright

# === CONFIG ===
SECTION_SELECTOR = "#main"  # Change if needed


def find_html_file():
    """Auto-detect HTML file in project root."""
    root = os.getcwd()
    html_files = [f for f in os.listdir(root) if f.endswith(".html")]

    if not html_files:
        raise FileNotFoundError("❌ No HTML file found in project root.")

    if "index.html" in html_files:
        return "index.html"

    return html_files[0]


def create_output_directory():
    """Ensure screenshots/YYYY-MM-DD exists in project root."""
    root = os.getcwd()
    date_folder = datetime.now().strftime("%Y-%m-%d")

    output_dir = os.path.join(root, "screenshots", date_folder)
    os.makedirs(output_dir, exist_ok=True)

    return output_dir


def extract_section_name(selector: str):
    """Convert selector to clean name."""
    if selector.startswith("#"):
        return selector.replace("#", "")
    elif selector.startswith("."):
        return selector.replace(".", "")
    return "section"


def main():
    # === Setup paths ===
    html_file = find_html_file()
    output_dir = create_output_directory()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    section_name = extract_section_name(SECTION_SELECTOR)

    file_url = "file://" + os.path.abspath(html_file)

    print(f"📄 Using HTML file: {html_file}")
    print(f"📁 Output directory: {output_dir}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # === FULL WIDTH (Desktop) ===
        page.set_viewport_size({"width": 1280, "height": 800})
        page.goto(file_url)
        page.wait_for_load_state("networkidle")

        full_width_path = os.path.join(
            output_dir,
            f"full_width_full_{timestamp}.png"
        )

        page.screenshot(path=full_width_path, full_page=True)
        print(f"✅ Saved: {full_width_path}")

        # === HALF WIDTH (Portrait / Mobile) ===
        page.set_viewport_size({"width": 375, "height": 812})
        page.goto(file_url)
        page.wait_for_load_state("networkidle")

        half_width_path = os.path.join(
            output_dir,
            f"half_width_full_{timestamp}.png"
        )

        page.screenshot(path=half_width_path, full_page=True)
        print(f"✅ Saved: {half_width_path}")

        # === SECTION SCREENSHOT ===
        page.set_viewport_size({"width": 1280, "height": 800})
        page.goto(file_url)
        page.wait_for_load_state("networkidle")

        try:
            element = page.locator(SECTION_SELECTOR)
            section_path = os.path.join(
                output_dir,
                f"section_{section_name}_{timestamp}.png"
            )
            element.screenshot(path=section_path)
            print(f"✅ Saved: {section_path}")
        except Exception:
            print(f"⚠️ Selector '{SECTION_SELECTOR}' not found. Skipping section screenshot.")

        browser.close()

    print("\n🎉 Screenshot automation complete.")


if __name__ == "__main__":
    main()
