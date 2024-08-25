// Use your own OpenWeatherMap API Key below
const WeatherapiKey = "ba709d103b7e6d17863e0719730abd39";
const GeolocationapiKey="c23e344f3fcc41cd8d3de34f59866df2";

const weatherContainer = document.getElementById("temperature");
const winddiv= document.getElementById("windandhumidity");
const clouds= document.getElementById("clouds");
const citydiv = document.getElementById("city");
const error = document.getElementById('error');
const alertdiv=document.getElementById('alertsSection');
const units = 'metric'; //can be imperial or metric
let temperatureSymobol =  (units == 'imperial') ? "°F" : "°C";

// fetching position of the user(longitude and latitude)
if(navigator.geolocation){
    navigator.geolocation.getCurrentPosition(
        (position)=>{
            // console.log(position); returns an object with coords as one element which latitude and longitude
            const {latitude,longitude}=position.coords;
            console.log(latitude,longitude);
            getaddress(latitude,longitude);

        },
        (error)=>{
            console.log(error);
        }
    );
}

const getaddress=async (latitude,longitude) => {
    try {
        const address=await fetch(`https://api.opencagedata.com/geocode/v1/json?q=${latitude}%2C${longitude}&key=${GeolocationapiKey}`);   
        
        const resp=await address.json();
        console.log("address",resp.results[0].formatted);

        const {city,state,country,postcode}=resp.results[0].components;

        // console.log(city,state,country,postcode)

        document.getElementById("Geolocation").innerHTML=`
        <pre>
        City : ${city} , Postcode : ${postcode}
        State : ${state}
        Country :${country}
        </pre>
        `

        document.querySelector(".fetchWeather").addEventListener("click",() => {
            fetchWeather(city);
        }
        )
    } catch (error) {
        console.log(error);
    }
}

// http://api.weatherapi.com/v1/forecast.json?lat=${latitude}&lon=${longitude}&appid=${WeatherapiKey}

async function fetchWeather(city){
    try {
        weatherContainer.innerHTML = '';
        error.innerHTML = '';
        city.innerHTML = '';
        
        const cnt = 10;
        // const apiUrl =`https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${WeatherapiKey}&units=${units}&cnt=${cnt}`;
        
        const apiUrl =`https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${WeatherapiKey}&units=${units}&cnt=${cnt}`;
        console.log(apiUrl);
        const response = await fetch(apiUrl);
        const data = await response.json();

        // console.log(data.list);
        //Display error if user types invalid city or no city
        if (data.cod == '400' || data.cod == '404') {
            error.innerHTML = `Cannot fetch location`;
            return;
        }

        // Display city name based on latitude and longitude
        citydiv.innerHTML = `Weather Report for ${data.city.name}`;

        weatherContainer.innerHTML="Predicted temperatures :"
        //Display weather data for each 3 hour increment
        data.list.forEach(hourlyWeatherData => {
            const hourlyWeatherDataDiv = createWeatherDescription(hourlyWeatherData);
            weatherContainer.appendChild(hourlyWeatherDataDiv);
        });

        winddiv.innerHTML=`<div class="windspeed">Wind Speed : ${data.list[0].wind.speed} metre/sec </div>
                            <div class="humidity">Humidity level : ${data.list[0].main.humidity}</div>`
        // data.list[0].wind.speed

        clouds.innerHTML=`<div>Weather Condition : ${data.list[0].weather[0].description}`
        // console.log(data.list[0].weather[0].description);
    } catch (error) {
        error.innerHTML = `Cannot fetch location`;
    }
}

function convertToLocalTime(dt) {

    // Create a new Date object by multiplying the Unix timestamp by 1000 to convert it to milliseconds
    // Will produce a time in the local timezone of user's computer
    const date = new Date(dt * 1000);

    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0'); // Months are 0-based, so add 1
    const day = String(date.getDate()).padStart(2, '0');
    const hours = String(date.getHours() % 12 || 12).padStart(2, '0'); // Convert 24-hour to 12-hour format
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');
    const period = date.getHours() >= 12 ? 'PM' : 'AM'; // Determine AM/PM

    // Formatted date string in the format: YYYY-MM-DD hh:mm:ss AM/PM
    return `${year}-${day}/${month}- ${hours}:${minutes}:${seconds} ${period}`;

}

function createWeatherDescription(weatherData) {
    const { main, dt } = weatherData;

    const description = document.createElement("div");
    const convertedDateAndTime = convertToLocalTime(dt);
    // console.log(main);
    // '2023-11-07 07:00:00 PM'
    description.innerHTML = `
        <div class = "weather_description">
        ${convertedDateAndTime.substring(5, 10)}${convertedDateAndTime.substring(10)}-${main.temp}${temperatureSymobol}
        </div>
    `;
    return description;
}