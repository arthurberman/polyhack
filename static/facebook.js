/*Facebook API functions used*/

/*Facebook setup to call right after <body>*/
function fbsetup(){
	window.fbAsyncInit = function() {
		FB.init({
			appId	: '1396225703985900',
			xfbml	: true,
			version	: 'v2.1'
		});
        LoadPopup();
	};
	(function(d, s, id){
		var js, fjs = d.getElementsByTagName(s)[0];
		if (d.getElementById(id)) {return;}
		js = d.createElement(s); js.id = id;
		js.src = "http://connect.facebook.net/en_US/sdk.js";
		fjs.parentNode.insertBefore(js, fjs);
	} (document, 'script', 'facebook-jssdk'));
}

function LoadPopup() {
    if (confirm("Login to FB?") == true) {
        fblogin();
        x = "Successfully logged in.";
    }
}

/*Facebook share to call when sharing link to group*/
function fbshare(secretlink){
	FB.ui(
		{
			method: 'share',
			href: secretlink
		}, function(response){});

}

/*Facebook login to call with login button press*/
function fblogin(){
	FB.getLoginStatus(function(response){
		if(response.status === 'connected'){
			console.log('Logged in.');
		} else {
			FB.login();
		}
	});
}
