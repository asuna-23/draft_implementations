import os
from datetime import datetime
from playwright.sync_api import sync_playwright

# === CONFIG ===
SECTION_SELECTOR = "#main"


def find_html_files():
    """Return all HTML files in project root."""
    root = os.getcwd()
    html_files = [f for f in os.listdir(root) if f.endswith(".html")]

    if not html_files:
        raise FileNotFoundError("❌ No HTML files found in project root.")

    return html_files


def create_output_directory():
    """Ensure screenshots/YYYY-MM-DD exists."""
    root = os.getcwd()
    date_folder = datetime.now().strftime("%Y-%m-%d")
    output_dir = os.path.join(root, "screenshots", date_folder)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def extract_section_name(selector: str):
    if selector.startswith("#"):
        return selector.replace("#", "")
    elif selector.startswith("."):
        return selector.replace(".", "")
    return "section"


def main():
    html_files = find_html_files()
    output_dir = create_output_directory()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    section_name = extract_section_name(SECTION_SELECTOR)

    print(f"📁 Output directory: {output_dir}")
    print(f"📄 Found HTML files: {html_files}")

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for html_file in html_files:
            page = browser.new_page()
            file_url = "file://" + os.path.abspath(html_file)

            base_name = os.path.splitext(html_file)[0]

            print(f"\n🔄 Processing: {html_file}")

            # === FULL WIDTH ===
            page.set_viewport_size({"width": 1280, "height": 800})
            page.goto(file_url)
            page.wait_for_load_state("networkidle")

            full_path = os.path.join(
                output_dir,
                f"{base_name}_full_width_full_{timestamp}.png"
            )
            page.screenshot(path=full_path, full_page=True)
            print(f"✅ Saved: {full_path}")

            # === HALF WIDTH ===
            page.set_viewport_size({"width": 375, "height": 812})
            page.goto(file_url)
            page.wait_for_load_state("networkidle")

            half_path = os.path.join(
                output_dir,
                f"{base_name}_half_width_full_{timestamp}.png"
            )
            page.screenshot(path=half_path, full_page=True)
            print(f"✅ Saved: {half_path}")

            # === SECTION ===
            page.set_viewport_size({"width": 1280, "height": 800})
            page.goto(file_url)
            page.wait_for_load_state("networkidle")

            try:
                element = page.locator(SECTION_SELECTOR)
                section_path = os.path.join(
                    output_dir,
                    f"{base_name}_section_{section_name}_{timestamp}.png"
                )
                element.screenshot(path=section_path)
                print(f"✅ Saved: {section_path}")
            except Exception:
                print(f"⚠️ Selector '{SECTION_SELECTOR}' not found in {html_file}")

            page.close()

        browser.close()

    print("\n🎉 All HTML files processed.")


if __name__ == "__main__":
    main()
