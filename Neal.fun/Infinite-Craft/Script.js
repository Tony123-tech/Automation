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
