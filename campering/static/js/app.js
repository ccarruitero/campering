var app = {
    init: function() {
        var map = L.mapbox.map('map', Settings.mapboxId);
        if ('geolocation' in navigator) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var lat = position.coords.latitude,
                    lng = position.coords.longitude;

                map.setView([lat, lng], 13);
                var marker = L.marker([lat, lng]).addTo(map);
            });
        } else {
            map.setView([-12.132292, -77.021588], 13);
        }
    }
}

app.init();
