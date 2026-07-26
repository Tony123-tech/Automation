(async function hyperFastBugFreeCrafter() {
    const delay = ms => new Promise(res => setTimeout(res, ms));
    const craftX = 500;
    const craftY = 500;

    while (true) {
        let allItems = Array.from(document.querySelectorAll('.sidebar .item, .items .item'));

  
        let items = allItems.filter(el => {
            if (!el || !el.innerText) return false;
            const name = el.innerText.trim();
            if (name === "" || name.toLowerCase().includes('search') || name.toLowerCase().includes('clear')) return false;

      
            const hasDiscoveryIcon = el.querySelector('.discovery, [class*="discovery"], [class*="icon"], i') !== null;
            const hasDiscoveryText = el.innerHTML.toLowerCase().includes('discovery') || el.innerHTML.includes('🌟') || el.innerHTML.includes('first');
            return !(hasDiscoveryIcon || hasDiscoveryText);
        });
        if (items.length < 2) {
            items = allItems.filter(el => {
                const name = el.innerText.trim();
                if (name === "" || name.toLowerCase().includes('search')) return false;
                return !el.innerHTML.toLowerCase().includes('discovery') && !el.innerHTML.includes('🌟');
            });
        }
        if (items.length < 2) {
            await delay(200);
            continue;
        }

        let idx1 = Math.floor(Math.random() * items.length);
        let idx2 = Math.floor(Math.random() * items.length);
        if (idx1 === idx2) continue;

        let elemA = items[idx1];
        let elemB = items[idx2];

        try {
            let rectA = elemA.getBoundingClientRect();
            elemA.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, clientX: rectA.left + 5, clientY: rectA.top + 5 }));
            document.dispatchEvent(new MouseEvent('mousemove', { bubbles: true, clientX: craftX, clientY: craftY }));
            document.dispatchEvent(new MouseEvent('mouseup', { bubbles: true, clientX: craftX, clientY: craftY }));
            let rectB = elemB.getBoundingClientRect();
            elemB.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, clientX: rectB.left + 5, clientY: rectB.top + 5 }));
            document.dispatchEvent(new MouseEvent('mousemove', { bubbles: true, clientX: craftX, clientY: craftY }));
            document.dispatchEvent(new MouseEvent('mouseup', { bubbles: true, clientX: craftX, clientY: craftY }));
            await delay(400);
        } catch (err) {
            await delay(100);
        }
    }
})();
