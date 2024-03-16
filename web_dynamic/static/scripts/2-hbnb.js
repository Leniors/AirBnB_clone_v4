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
