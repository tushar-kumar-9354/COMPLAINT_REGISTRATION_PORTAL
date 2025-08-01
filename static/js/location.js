/* static/js/location.js */
let map;
let marker;

function getLocation() {
  if (!navigator.geolocation) {
    alert("Geolocation is not supported by your browser.");
    return;
  }

  navigator.geolocation.getCurrentPosition(
    (pos) => {
      const lat = pos.coords.latitude;
      const lng = pos.coords.longitude;

      // Reveal the map container
      document.getElementById("map").style.display = "block";

      // First-time map setup
      if (!map) {
        map = L.map("map").setView([lat, lng], 15);
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          attribution: "© OpenStreetMap contributors",
        }).addTo(map);
      } else {
        map.setView([lat, lng], 15);
      }

      // Add or move marker
      if (marker) {
        marker.setLatLng([lat, lng]);
      } else {
        marker = L.marker([lat, lng])
          .addTo(map)
          .bindPopup("You are here")
          .openPopup();
      }
    },
    (err) => {
      alert("Unable to retrieve your location: " + err.message);
    }
  );
}
