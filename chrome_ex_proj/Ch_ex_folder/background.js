function saveTime(site, time) {
    fetch("http://127.0.0.1:8000/api/save/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            website: site,
            time: Math.floor(time / 1000)
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to save data");
        }
        return response.json();
    })
    .then(data => {
        console.log("Saved successfully:", data);
    })
    .catch(error => {
        console.error("Error saving time:", error);
    });
}