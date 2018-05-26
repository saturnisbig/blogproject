$(function() {
$('#convert-rgbcolor').click(function() {
	var color = $('#rgbcolor').val();
	if (color.length == 0) {
		alert("颜色值不能为空！");
		return;
	}
	var csrf = $(this).data('csrf');
	var convert_type = $(this).data('convert-type');
	var url = $(this).data('ajax-url');
	$.ajaxSetup({
		data: {
			'csrfmiddlewaretoken': csrf
		}
	});
	$.ajax({
		type: 'post',
		url: url,
		data: {
			'convert_type': convert_type,
			'color': color,
		},
		dataType: 'json',
		success: successFunc,
		error: function() {
			alert('转换失败');
		}

	});
	function successFunc(ret){
		var json = eval(ret);
		//alert(json);
		var result = json.result;
		var bcolor = json.base_color
		var msg = json.msg;
		var text = result + '<br />' + bcolor + '<br />' + msg + '<br/>';
		$("#rgb-result").html(text);
	}
});
$('#convert-hexcolor').click(function() {
	var color = $('#hexcolor').val();
	if (color.length == 0) {
		alert("颜色值不能为空！");
		return;
	}
	var csrf = $(this).data('csrf');
	var convert_type = $(this).data('convert-type');
	var url = $(this).data('ajax-url');
	$.ajaxSetup({
		data: {
			'csrfmiddlewaretoken': csrf
		}
	});
	$.ajax({
		type: 'post',
		url: url,
		data: {
			'convert_type': convert_type,
			'color': color,
		},
		dataType: 'json',
		success: successFunc,
		error: function() {
			alert('转换失败，请检查输入');
		}

	});
	function successFunc(ret){
		var json = eval(ret);
		//alert(json);
		var result = json.result;
		var bcolor = json.base_color
		var msg = json.msg;
		var text = result + '<br />' + bcolor + '<br />' + msg + '<br/>';
		$("#hex-result").html(text);
	}
});
	/*
		var base_t = sessionStorage.getItem('base_t');
		var now_t = Date.parse(new Date());
		if (base_t) {
			var tt = now_t - base_t;
			if (tt < 40000) {
				alert('两次评论时间间隔必须大于40秒，还需等待' + (40 - parseInt(tt / 1000)) + '秒');
				return;
			} else {
				sessionStorage.setItem('base_t', now_t);
			}
		} else {
			sessionStorage.setItem('base_t', now_t)
		};
		*/
})
