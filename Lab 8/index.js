function onDocumentLoad(){
	console.log(new Date() * 1000);
	const $form = $('.form');
	$('button').on('click',function(){
		var points = [];
		var from = parseInt($form.val());
		var to = parseInt($(".to").val());
		var $fun = $(".fun").val();
		for(var i = from; i < to; i = i + 0.1 ){
			const x = i;
			const fun = $fun;
			const y = eval(fun)
			points.push([x,y]);
		}
		$.plot($("#placeholder"), [{ label: $fun, data: points}] , { yaxis: {max: 1}, legend: {show: true, position: "nw"}});
		
	})
}

onDocumentLoad();
// $(onDocumentLoad);

function ReDraw(from, to, fun, points) {

}