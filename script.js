
 const apiKey = "9144afbcb1d6f7c526969cfe9bb666f2";
async function getWeather() {
    const city = document.getElementById("city").value;

    if (!city) {
        alert("Please enter a city name.");
        return;
    }

    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    const res = await fetch(url);
    const data = await res.json();

    if (data.cod === "404") {
        document.getElementById("weather-result").innerHTML =
            `<div class="alert alert-danger">City not found!</div>`;
        return;
    }

    document.getElementById("weather-result").innerHTML = `<img src="https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png">

        <div class="temp">${data.main.temp}°C</div>
        
        <div class="city">${data.name}</div>

        <p class="text-capitalize">${data.weather[0].description}</p>
        `;
        // Today Highlight

                document.getElementById("humidity").innerHTML = + data.main.humidity +"  "+ "%";
                document.getElementById("wind").innerHTML = + data.wind.speed +"  "+ "m/s";
                document.getElementById("pressure").innerHTML = + data.main.pressure +"  "+ "hPa";
                document.getElementById("cloud").innerHTML = + data.clouds.all +"  "+ "%";
                document.getElementById("rise").innerHTML = + data.sys.sunrise;
                document.getElementById("set").innerHTML = + data.sys.sunset;

        // 5 Day Forecast
        const forecastURL =
        `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${apiKey}&units=metric`;

    const forecastRes = await fetch(forecastURL);
    const forecastData = await forecastRes.json();

    const forecastDiv = document.getElementById("forecast");
    forecastDiv.innerHTML = ""; // clear previous forecast

    // One forecast each day at 12:00
    const daily = forecastData.list.filter(item =>
        item.dt_txt.includes("12:00:00")
    );

    daily.forEach(day => {
        const date = new Date(day.dt * 1000).toLocaleDateString("en-US", {
            month: "short",
            day: "numeric",
        });

        const temp = Math.round(day.main.temp);
        const icon = day.weather[0].icon;

        forecastDiv.innerHTML += `
            <div class="day5">
                <div class="date">${date}</div>
                <img src="https://openweathermap.org/img/wn/${icon}@2x.png">
                <div class="temp">${temp}°C</div>
            </div>
        `;
    });
}

