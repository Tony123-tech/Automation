# Infinite Craft Auto-Crafter Guide

This is an automation script for the game **Infinite Craft**. It automatically selects two different random elements from your unlocked item list, drags them to a central crafting area, and combines them. It includes smart filters to prevent game freezes caused by "First Discovery" pop-ups, allowing for non-stop recipe exploration.

---

## 🌟 Key Features
* **Hyper-Fast Crafting**: Attempts a new combination every 300 milliseconds.
* **Smart Filtering**: Automatically ignores the search bar, reset button, and elements with "Discovery" or "🌟" icons to prevent popup lock-ups.
* **Background Auto-Refresh**: Scans your sidebar every 5 seconds to instantly include newly unlocked items into the crafting loop.
* **Anti-Stacking Mechanism**: Applies small random position offsets so items do not stack perfectly on top of each other and bug out the drag-and-drop detection.

---

## 🛠️ How to Use

### Step 1: Copy the Script
Copy the exact JavaScript code snippet below:

```javascript
(async function hyperFastBugFreeCrafterV2() {
    const delay = ms => new Promise(res => setTimeout(res, ms));
    const craftX = 500;
    const craftY = 500;
    let cachedItems = [];
    function updateItemsCache() {
        let allItems = Array.from(document.querySelectorAll('.sidebar .item, .items .item'));
        let filtered = allItems.filter(el => {
            if (!el || !el.innerText) return false;
            const name = el.innerText.trim();
            if (name === "" || name.toLowerCase().includes('search') || name.toLowerCase().includes('clear')) return false;
            const hasDiscoveryIcon = el.querySelector('.discovery, [class*="discovery"], [class*="icon"], i') !== null;
            const hasDiscoveryText = el.innerHTML.toLowerCase().includes('discovery') || el.innerHTML.includes('🌟') || el.innerHTML.includes('first');
            return !(hasDiscoveryIcon || hasDiscoveryText);
        });
        if (filtered.length < 2) {
            filtered = allItems.filter(el => {
                const name = el.innerText.trim();
                if (name === "" || name.toLowerCase().includes('search')) return false;
                return !el.innerHTML.toLowerCase().includes('discovery') && !el.innerHTML.includes('🌟');
            });
        }
        cachedItems = filtered;
    }
    updateItemsCache();
    const cacheInterval = setInterval(updateItemsCache, 5000);
    function triggerDragDrop(element, targetX, targetY) {
        let rect = element.getBoundingClientRect();
        element.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, clientX: rect.left + 5, clientY: rect.top + 5 }));
        document.dispatchEvent(new MouseEvent('mousemove', { bubbles: true, clientX: targetX, clientY: targetY }));
        document.dispatchEvent(new MouseEvent('mouseup', { bubbles: true, clientX: targetX, clientY: targetY }));
    }
    try {
        while (true) {
            if (cachedItems.length < 2) {
                await delay(200);
                continue;
            }
            let idx1 = Math.floor(Math.random() * cachedItems.length);
            let idx2 = Math.floor(Math.random() * (cachedItems.length - 1));
            if (idx2 >= idx1) idx2++;
            let elemA = cachedItems[idx1];
            let elemB = cachedItems[idx2];
            try {
                let offsetX = (Math.random() - 0.5) * 10;
                let offsetY = (Math.random() - 0.5) * 10;
                triggerDragDrop(elemA, craftX + offsetX, craftY + offsetY);
                triggerDragDrop(elemB, craftX + offsetX, craftY + offsetY);
                await delay(300);
            } catch (err) {
                await delay(100);
            }
        }
    } finally {
        clearInterval(cacheInterval);
    }
})();
```

### Step 2: Run it in Your Browser
1. Open your browser and go to [Infinite Craft](https://neal.fun/infinite-craft).
2. Right-click anywhere on the page and select **Inspect** (or press the keyboard shortcut):
   * **Windows / Linux**: `F12` or `Ctrl + Shift + I`
   * **Mac**: `Cmd + Option + I`
3. Click on the **Console** tab at the top of the developer tools panel.
4. Paste the copied code into the console input line.
5. Press **`Enter`**. The script will start running immediately!

---

## 🛑 How to Stop the Script

To halt the automation, use one of the following methods:
1. **Refresh the Page**: Press `F5` (or `Cmd + R` on Mac) to reload the website. This completely wipes the running script memory.
2. **Close the Tab**: Simply close the browser tab running Infinite Craft.

---

## ⚙️ Advanced Customization (Optional)
If you want to tweak how the script runs, you can modify these numbers in the code before hitting Enter:

* **Change Crafting Speed**: Locate `await delay(300);` near the bottom. Change `300` to a higher number like `500` (0.5 seconds) if your browser is lagging or if the game cannot keep up.
* **Change Screen Coordinates**: Locate `const craftX = 500;` and `const craftY = 500;` at the top. If you are using a smaller display or laptop, you can adjust these X and Y coordinates to move the crafting drop zone to the center of your screen.
