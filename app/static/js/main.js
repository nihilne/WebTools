function copyKey(button) {
    const key = document.getElementById("generated-key").innerText;
    navigator.clipboard.writeText(key).then(() => {
        if (!button.dataset.originalText) {
            button.dataset.originalText = button.innerText;
        }
        button.innerText = "Copied!";
        clearTimeout(button.dataset.timeoutId);
        const timeoutId = setTimeout(() => {
            button.innerText = button.dataset.originalText;
        }, 3000);
        button.dataset.timeoutId = timeoutId;
    });
}