$( document ).ready(function() {
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
