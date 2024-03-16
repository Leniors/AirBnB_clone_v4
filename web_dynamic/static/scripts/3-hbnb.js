$( document ).ready(function() {

	fetch('http://127.0.0.1:5001/api/v1/status/')
		.then(response => response.json())
		.then(data => {
			if (data.status === 'OK') {
				$('#api_status').addClass('available');
			} else {
				$('#api_status').removeClass('available');
			}
		}).catch(error => console.error('Error:', error));

	const options = {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({})
	}
	fetch('http://127.0.0.1:5001/api/v1/places_search/', options)
		.then(response => response.json())
		.then(data => {
			console.log(data);
			data.forEach((place) => {
				$('.places').append(
					`<article>
					<div class="headline">
					<h2 class="article_title">${place.name}</h2>
					<div class="price_by_night">$${place.price_by_night}</div>
					</div>
					<div class="information">
					<div class="max_guest">
					<div class="guest_icon"></div>
					<p>${place.max_guest} Guests</p>
					</div>
					<div class="number_rooms">
					<div class="bed_icon"></div>
					<p>${place.number_rooms} Bedroom</p>
					</div>
					<div class="number_bathrooms">
					<div class="bath_icon"></div>
					<p>${place.number_bathrooms} Bathroom</p>
					</div>
					</div>
					<div class="user"><b>Owner</b>: John Lennon</div>
					<div class="description">${place.description}
					</div>
					<div class="amenities">
					<h2 class="article_subtitle">Amenities</h2>
					<ul>
					</ul>
					</div>
					<div class="reviews">
					</div>
					</article>`);
			});
		}).catch(error => console.error('Error:', error));

	let selectedAmenities = {};

	$('input[type="checkbox"]').change(function() {
		let amenityID = $(this).data('id');
		let amenityName = $(this).data('name');

		if ($(this).is(':checked')) {
			selectedAmenities[amenityID] = amenityName;
		} else {
			delete selectedAmenities[amenityID];
		}

		let amenitiesList = Object.values(selectedAmenities).join(', ');
		$('.filter_amenities h4:first').text(amenitiesList || 'No amenities selected.');
	});
});
