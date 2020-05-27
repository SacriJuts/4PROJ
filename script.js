// This method will trigger user permissions
Html5Qrcode.getCameras().then(devices => {
/**
* devices would be an array of objects of type:
* { id: "id", label: "label" }
*/
if (devices && devices.length) {
	var cameraId = devices[0].id;
	// .. use this to start scanning.
	const html5QrCode = new Html5Qrcode(/* element id */ "reader", true);
	html5QrCode.start(
		cameraId, 
		{
			fps: 10,    // Optional frame per seconds for qr code scanning
			qrbox: 250  // Optional if you want bounded box UI
		},
		qrCodeMessage => {
			
			console.log("QR code found !");
			
			// do something when code is read
		},
		errorMessage => {
			// parse error, ignore it.
		})
	.catch(err => {
		// Start failed, handle it.
	});
	}
}).catch(err => {
  // handle err
});

