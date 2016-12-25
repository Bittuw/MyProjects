var sec = 0;
var exit = "{{ button_exit }}"


if ("{{ button_exit }}" == "True") {
		$('#addbtn').append("<button class=\"btn btn-default\" onclick=\"location.href=\'../exit\'\">Выйти</button>");
}

init();



function init() {
	setInterval(tick, 1000);
}

function tick() {
	sec++;
	document.getElementById('time').value = sec;
}