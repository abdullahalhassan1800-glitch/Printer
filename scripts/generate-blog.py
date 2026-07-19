import os
import json
import random
import datetime
from pathlib import Path

POSTS_DIR = Path(__file__).resolve().parent.parent / "_posts"

CONTENT_TEMPLATES = {
    "Printer Not Printing Black Ink – Causes and Fixes": {
        "categories": "Troubleshooting Guide",
        "content": """Is your printer not printing black ink even though cartridges have ink? This is a frustratingly common issue with inkjet printers. Before you replace anything, try these proven solutions.

### Why Printer Not Printing Black Ink Happens

The most common causes include:
- **Clogged printhead nozzles:** Black ink dries up and blocks the nozzles when the printer sits unused.
- **Empty or low black ink cartridge:** The printer may still show ink if a chip is defective.
- **Printhead alignment issues:** Misaligned printheads skip black ink during printing.
- **Driver or software problems:** Incorrect print settings force the printer to use color ink only.
- **Air bubbles in ink system:** After replacing a cartridge, air can block ink flow.

### Step 1: Run Printhead Cleaning

Go to your printer's maintenance menu and run the **printhead cleaning** cycle 2-3 times. Print a nozzle check pattern after each cycle. This clears dried ink from the nozzles.

### Step 2: Check Ink Levels

Open your printer's companion app or printer properties and verify black ink levels. If low, replace with a genuine manufacturer cartridge. Third-party cartridges often cause this problem.

### Step 3: Use the Right Print Settings

In your print dialog, select "Plain Paper" and "Black & White" or "Grayscale" printing. Some settings force the printer to mix colors to create black.

### Step 4: Manual Printhead Cleaning

If automatic cleaning doesn't work, remove the printhead and clean the copper contacts and nozzles gently with distilled water and a lint-free cloth. Let it dry completely before reinstalling.

### Step 5: Update Printer Drivers

Outdated drivers can cause the printer to misread ink levels. Download the latest driver from your printer manufacturer's official website and reinstall.

<div class="blog-cta">
  <h3>Still Having Black Ink Problems?</h3>
  <p>Check your printer manufacturer's official support website for the latest drivers and troubleshooting guides for your specific printer model.</p>
  <a href="{{ site.baseurl }}/services/" class="btn btn-primary">View All Printer Reviews</a>
</div>"""
    },
    "How to Fix Printer Error 0x97 – Mainboard Issue": {
        "categories": "Troubleshooting Guide",
        "content": """Printer error code 0x97 is one of the most feared errors among printer users. This error typically indicates a mainboard or ink system issue. Here's how to diagnose and fix it.

### What Does Error 0x97 Mean?

Error 0x97 appears on business, tank, photo, and wide-format printers. It generally means:
- **Mainboard failure:** The printer's main logic board has detected a fault.
- **Ink system malfunction:** The ink pump, waste ink pad, or sensor has failed.
- **Carriage mechanism issue:** The printhead carriage is stuck or obstructed.

### Step 1: Power Cycle the Printer

Turn off the printer, unplug it from power, and wait 5 full minutes. Plug it back in and turn it on. This clears temporary sensor errors.

### Step 2: Check for Obstructions

Open the printer cover and check if anything is blocking the printhead carriage. Remove any paper scraps, staples, or debris. Gently move the carriage manually to ensure it moves freely.

### Step 3: Run Your Printer's Diagnostic Tool

Download and run your printer's diagnostic tool from your computer. Check for error details and run a head cleaning if available.

### Step 4: Reset Using a Waste Ink Reset Tool

For advanced users, a waste ink reset utility can reset the waste ink counter and clear error 0x97. This requires connecting the printer via USB.

### Step 5: Check Ink System

If the error persists, the waste ink pad may be full or the ink pump may be faulty. These require replacement by a technician.

<div class="blog-cta">
  <h3>Error 0x97 Not Fixed?</h3>
  <p>Visit your printer manufacturer's official support site for detailed troubleshooting guides and diagnostic tools for the 0x97 error.</p>
  <a href="{{ site.baseurl }}/services/" class="btn btn-primary">View All Printer Reviews</a>
</div>"""
    },
    "Printer Drum Error – How to Reset and Fix": {
        "categories": "Troubleshooting Guide",
        "content": """Printer drum errors can stop you from printing completely. If you see "Drum Error," "Replace Drum," or "Drum Stop" messages, here's how to fix it.

### Understanding Printer Drum Errors

Laser printers use a separate drum unit and toner cartridge. Common drum errors include:
- **Drum End Soon:** The drum is approaching its end of life.
- **Replace Drum:** The drum counter has reached its limit.
- **Drum Stop:** The printer has stopped functioning due to drum issues.
- **Drum Error:** A communication error with the drum unit.

### Method 1: Reset the Drum Counter

Most laser printers let you reset the drum counter manually:
1. Open the front cover.
2. Press and hold the **OK** or **Clear/Back** button for 5 seconds.
3. Use the arrow keys to select "Reset Drum" or "Drum Reset."
4. Press OK to confirm.
5. Close the cover.

### Method 2: Clean the Drum Unit

Remove the drum unit and toner cartridge together. Gently clean the green drum surface with a dry, lint-free cloth (do not touch the drum surface with bare fingers). Also clean the metal contacts on both sides.

### Method 3: Replace Drum Unit

If cleaning and resetting don't work, the drum unit has reached its actual end of life. Replace it with a genuine manufacturer drum unit compatible with your model.

### Preventing Future Drum Errors

- Use genuine manufacturer toner and drum units.
- Keep the printer in a clean, dust-free environment.
- Reset the drum counter each time you replace the drum unit.

<div class="blog-cta">
  <h3>Drum Error Still There?</h3>
  <p>Visit your printer manufacturer's official support website for model-specific drum reset instructions and troubleshooting guides.</p>
  <a href="{{ site.baseurl }}/services/" class="btn btn-primary">View All Printer Reviews</a>
</div>"""
    },
    "Printer B200 Error – Step-by-Step Fix Guide": {
        "categories": "Troubleshooting Guide",
        "content": """The printer B200 error is one of the most common and frustrating errors on consumer and business printers. This error indicates a printhead or ink system problem.

### What Causes Error B200?

Error B200 typically means:
- **Printhead failure:** The printhead has malfunctioned or short-circuited.
- **Ink system issue:** Air bubbles or clogged ink pathways.
- **Mainboard communication error:** The printer cannot communicate with the printhead properly.

### Step 1: Hard Reset Your Printer

1. Turn off the printer and unplug it from power.
2. Wait 10 minutes (this is important for capacitors to discharge).
3. Plug it back in and turn on.
4. If the error is gone, it was a temporary glitch.

### Step 2: Remove and Reinstall Printhead

1. Open the printer cover. The printhead carriage will move to the center.
2. Remove the ink cartridges first.
3. Lift the green/blue locking lever and remove the printhead.
4. Clean the printhead contacts with a dry lint-free cloth.
5. Also clean the carriage contacts inside the printer.
6. Reinstall the printhead firmly, lower the lever, and reinsert cartridges.

### Step 3: Check for Ink Spills

Ink spills inside the printer can cause electrical shorts that trigger B200. Open the printer and look for any ink on the contacts, carriage, or mainboard area. Clean carefully with a lint-free cloth.

### Step 4: Replace the Printhead

If steps 1-3 don't work, the printhead is likely damaged. Replace it with a genuine manufacturer printhead compatible with your model.

> **Warning:** Never use third-party or refilled ink cartridges. They frequently cause the B200 error by damaging the printhead.

<div class="blog-cta">
  <h3>B200 Error Not Fixed?</h3>
  <p>Check your printer manufacturer's official support website for model-specific troubleshooting and the latest firmware updates.</p>
  <a href="{{ site.baseurl }}/services/" class="btn btn-primary">View All Printer Reviews</a>
</div>"""
    },
    "Printer Keeps Going Offline – Here's the Permanent Fix": {
        "categories": "Troubleshooting",
        "content": """Does your printer keep going offline randomly? You start a print job, and Windows tells you the printer is offline. This is one of the most frustrating printer problems. Here's how to fix it permanently.

### Why Printers Keep Going Offline

The most common reasons include:
- **WiFi signal instability:** The printer loses connection to the network briefly.
- **Power saving settings:** The printer goes to sleep and doesn't wake up properly.
- **Driver conflicts:** Multiple printer drivers cause Windows to lose communication.
- **Router DHCP issues:** The printer's IP address changes after a router restart.
- **Windows print spooler crashes:** A stuck print job takes down the spooler.

### Fix 1: Assign a Static IP Address

The most effective permanent fix is to assign a static IP to your printer:
1. Print a network configuration page from your printer menu.
2. Note the current IP address, subnet mask, and gateway.
3. Open your router settings and reserve this IP for your printer's MAC address.
4. Alternatively, set a static IP directly in the printer's network settings.

### Fix 2: Disable Printer Power Saving

On your printer's menu, navigate to Settings > Power Saving or Sleep Mode. Disable or extend the sleep timer to 2+ hours. This prevents the printer from going into deep sleep mode.

### Fix 3: Update Network Drivers

Outdated WiFi or Ethernet drivers on your computer can cause intermittent disconnections. Update your network adapter drivers from Device Manager.

### Fix 4: Clear Print Spooler Corruptions

Run these steps when the printer goes offline:
1. Open Services (services.msc), stop "Print Spooler."
2. Delete all files in `C:\\\\Windows\\\\System32\\\\spool\\\\PRINTERS\\\\`.
3. Restart the Print Spooler service.

### Fix 5: Run Manufacturer Diagnostic Tool

- Run your printer manufacturer's diagnostic tool (check your printer's documentation or manufacturer website for the correct utility).

<div class="blog-cta">
  <h3>Printer Still Going Offline?</h3>
  <p>Check your printer manufacturer's official support website for model-specific troubleshooting guides and diagnostic tools.</p>
  <a href="{{ site.baseurl }}/services/" class="btn btn-primary">View Printer Reviews</a>
</div>"""
    },
    "How to Connect Printer to WiFi – Wireless Setup Guide": {
        "categories": "Setup Guide",
        "content": """Connecting your printer to WiFi allows you to print wirelessly from any device in your home or office. Here are three easy methods to set up your printer on your wireless network.

### Method 1: Use WiFi Protected Setup (WPS)

If your router has a WPS button, this is the fastest method:
1. Press the **WPS button** on your router for 3-5 seconds until the light starts blinking.
2. Within 2 minutes, press and hold the **WiFi button** on your printer for 3 seconds.
3. The printer will automatically connect to your network.
4. The WiFi light will turn solid green when connected.

### Method 2: Use the Printer's Wireless Setup Wizard

For printers with a touchscreen:
1. Press the **Home** button and navigate to **WiFi Setup** or **Network Settings**.
2. Select **Wireless LAN Setup** and choose **WiFi Setup Wizard**.
3. Select your WiFi network from the list.
4. Enter your WiFi password using the on-screen keyboard.
5. Press **Start Setup** to connect.

### Method 3: Use Your Printer's Companion App

Download your printer manufacturer's companion app from your phone's app store. The app will guide you through the wireless setup step by step and also helps with ink level monitoring and printer maintenance.

### Troubleshooting WiFi Connection

- **Printer not finding network:** Move the printer closer to the router.
- **Wrong password:** WiFi passwords are case-sensitive. Double-check.
- **Network band:** Most printers work best on 2.4GHz networks.
- **Router restart:** Unplug your router for 30 seconds and try again.

<div class="blog-cta">
  <h3>Stuck on WiFi Setup?</h3>
  <p>Visit your printer manufacturer's official support site for detailed WiFi setup guides and connection troubleshooting.</p>
  <a href="{{ site.baseurl }}/services/" class="btn btn-primary">View All Printer Reviews</a>
</div>"""
    },
    "Printer Paper Jam – How to Clear Properly": {
        "categories": "Troubleshooting",
        "content": """Paper jams are one of the most common printer problems. While they seem simple, improper removal can damage your printer. Here's the correct way to clear paper jams in any printer.

### Step 1: Turn Off the Printer

Always turn off the printer before removing jammed paper. This prevents damage to the rollers and other internal components.

### Step 2: Open All Access Doors

Open the main cover, rear access door, and paper tray. Look for jammed paper in all possible locations. Paper can tear and leave small pieces behind.

### Step 3: Remove Paper Gently

Pull the paper in the **direction of the paper path** (usually forward or upward). Never pull paper backward against the rollers. If the paper tears, remove all fragments carefully.

### Step 4: Check Rollers

After removing the jam, inspect the rollers for paper dust or residue. Clean them with a dry, lint-free cloth. Dirty rollers cause recurring paper jams.

### Step 5: Close All Doors Properly

Ensure all doors and trays are closed securely. An open door will cause the printer to show a jam error even after clearing the paper.

### Preventing Future Paper Jams

- **Don't overfill the paper tray:** Keep it at 75% capacity.
- **Use quality paper:** Cheap paper is more likely to jam.
- **Fan the paper:** Before loading, fan the paper stack to prevent pages from sticking.
- **Store paper properly:** Keep paper in a dry place away from humidity.
- **Clean rollers regularly:** Clean paper feed rollers monthly.

<div class="blog-cta">
  <h3>Paper Jam Still Not Clearing?</h3>
  <p>Check your printer manufacturer's official support website for additional paper jam troubleshooting guides and maintenance tips.</p>
  <a href="{{ site.baseurl }}/services/" class="btn btn-primary">View All Printer Reviews</a>
</div>"""
    },
    "Printer Faded Prints – How to Fix Print Quality Issues Fast": {
        "categories": "Print Quality",
        "content": """Are your prints coming out faded, streaky, or with lines? Print quality problems are one of the most common printer issues across all brands. Here's how to fix them.

### Common Causes of Faded Prints

- **Low ink or toner:** Cartridges are running out.
- **Clogged printhead nozzles:** Dried ink blocks the nozzles.
- **Wrong paper type setting:** Using photo paper settings on plain paper.
- **Low-quality ink:** Third-party or refilled cartridges.
- **Dirty printhead:** Dust and residue buildup.

### Fix 1: Check Ink or Toner Levels

Open your printer software (your printer's companion app or status monitor) and check ink levels. If any cartridge is low, replace it with a genuine manufacturer cartridge.

### Fix 2: Run Printhead Cleaning

Access the maintenance menu on your printer (consult your printer's manual for the exact menu path).

Run the cleaning cycle 2-3 times, printing a nozzle check pattern after each attempt.

### Fix 3: Align Printhead

After cleaning, run a printhead alignment from the printer menu. This ensures the printhead is properly positioned for accurate printing.

### Fix 4: Use Correct Paper Settings

In your print dialog, match the paper type setting to the actual paper in the tray. Using "Photo Paper" setting on plain paper causes ink to sit on top and smudge.

### When to Replace the Printhead

If cleaning doesn't work after 3-4 attempts, the printhead may need replacement. This is common on printers that haven't been used for 2+ weeks.

<div class="blog-cta">
  <h3>Print Quality Still Bad?</h3>
  <p>Check your printer manufacturer's official support site for advanced print quality troubleshooting guides.</p>
  <a href="{{ site.baseurl }}/services/" class="btn btn-primary">View Printer Reviews</a>
</div>"""
    },
    "How to Scan from Printer to Computer – Windows 11 Guide": {
        "categories": "Setup Guide",
        "content": """Scanning from your printer to a Windows 11 computer should be simple, but many users struggle with it. Here's every method to get your scanner working.

### Method 1: Use Windows Scan App (Easiest)

Windows 11 has a built-in Scan app:
1. Click Start and type "Scan" to open the **Windows Scan** app.
2. Place your document on the scanner glass.
3. Click the **Preview** button to see the scan area.
4. Adjust settings (color, resolution, file type).
5. Click **Scan** to save the document.

### Method 2: Use Manufacturer Software

- Download your printer manufacturer's scanning app from the Microsoft Store or their website (check your printer's documentation for the recommended scanning software).

These apps provide more features like multi-page scanning, OCR, and cloud upload.

### Method 3: Scan from Printer Control Panel

Place your document on the scanner glass, then on the printer's touchscreen:
1. Select **Scan** or **Scan to Computer**.
2. Choose the destination computer.
3. Select scan settings (color, resolution, file format).
4. Press **Start** to scan.

### Common Scanning Problems

- **Printer not detected:** Ensure the printer is on and connected to the same network.
- **Scanner not found:** Restart both printer and computer.
- **Poor scan quality:** Clean the scanner glass with a soft cloth.
- **Scan to email not working:** Check email settings in the printer menu.

<div class="blog-cta">
  <h3>Having Scanner Issues?</h3>
  <p>Check your scanner manufacturer's official support website for scanning setup guides and troubleshooting.</p>
  <a href="{{ site.baseurl }}/services/" class="btn btn-primary">View Printer Reviews</a>
</div>"""
    },
    "Printer Error State Windows 11 – Fix in 5 Minutes": {
        "categories": "Error Fix",
        "content": """Seeing "Printer in error state" on Windows 11? This error prevents you from printing anything. Here's how to fix it in 5 minutes.

### What Does "Printer in Error State" Mean?

Windows shows this error when it cannot communicate with the printer properly. The printer may be physically fine but the software connection is broken.

### Fix 1: Restart Everything (30 seconds)

Turn off your printer, unplug it for 30 seconds, then plug it back in and turn it on. Restart your computer. This fixes 70% of error state problems.

### Fix 2: Clear the Print Queue

1. Open **Settings > Bluetooth & Devices > Printers & Scanners**.
2. Select your printer and click **Open print queue**.
3. Click the **Printer** menu and uncheck **Use Printer Offline** if checked.
4. Cancel all stuck print jobs (right-click > Cancel).

### Fix 3: Restart Print Spooler Service

1. Press **Windows + R**, type `services.msc`, and press Enter.
2. Find **Print Spooler** in the list.
3. Right-click it and select **Restart**.
4. Verify the startup type is set to **Automatic**.

### Fix 4: Remove and Re-add Printer

1. Go to **Settings > Bluetooth & Devices > Printers & Scanners**.
2. Click your printer and select **Remove**.
3. Click **Add device** and let Windows detect your printer.
4. Follow the on-screen prompts to reinstall it.

### Fix 5: Run Printer Troubleshooter

Windows 11 has a built-in troubleshooter:
1. Go to **Settings > System > Troubleshoot**.
2. Click **Other troubleshooters**.
3. Find **Printer** and click **Run**.

<div class="blog-cta">
  <h3>Printer Error State Not Fixed?</h3>
  <p>Check your printer manufacturer's official support site for advanced troubleshooting and error state resolution guides.</p>
  <a href="{{ site.baseurl }}/contact/" class="btn btn-primary">Get Help Now</a>
</div>"""
    },
}


def generate_frontmatter(title, date_str, categories):
    tags = title.lower().replace(" – ", " ").replace("-", " ").replace("?", "").replace("'", "").replace(",", "")
    words = tags.split()
    important = [w for w in words if len(w) > 2][:5]
    tags_str = ", ".join(important)
    return f"""---
title: "{title}"
date: {date_str} -0500
categories: "{categories}"
tags: [{tags_str}]
image: "/images/printer-hero.jpg"
read_time: 6
---"""


def make_slug(title):
    slug = title.lower()
    slug = slug.replace(" – ", "-")
    slug = slug.replace("–", "-")
    slug = slug.replace(" ", "-")
    for ch in "?',.!():\"'":
        slug = slug.replace(ch, "")
    slug = slug.replace("---", "-").replace("--", "-")
    return slug.strip("-")


def main():
    today = datetime.date.today()
    date_str = today.strftime("%Y-%m-%d %H:%M:%S")

    for title, data in CONTENT_TEMPLATES.items():
        slug = make_slug(title)
        filename = f"{today.strftime('%Y-%m-%d')}-{slug}.md"
        filepath = POSTS_DIR / filename

        if filepath.exists():
            print(f"SKIP: {filename} (already exists)")
            continue

        frontmatter = generate_frontmatter(title, date_str, data["categories"])
        content = data["content"]
        full_content = f"{frontmatter}\n\n{content}\n"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(full_content)

        print(f"CREATED: {filename}")
        return

    print("DONE: All topics have been published. No new post generated.")


if __name__ == "__main__":
    main()
