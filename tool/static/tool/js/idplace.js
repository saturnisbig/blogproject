$(function() {
	$('#get-cardid').click(function(){
		var idnumber = $('#idnumber').val();
		if (idnumber.length == 0) {
			alert("身份证号不能为空");
			return;
		}
		var csrf = $(this).data('csrf');
		var url = $(this).data('ajax-url');
		$.ajaxSetup({
			data: {
				'csrfmiddlewaretoken': csrf
			}
		});
		$.ajax({
			type:'post',
			url: url,
			data: {
				'cardid': idnumber
			},
			dataType: 'json',
			success: function(ret){
				var json = eval(ret);
				var number = json.number
				var place = json.place;
				//var sex = json.sex;
				//var age = json.age;
				var msg = json.msg;
				//var text = place + '<br />' + sex + '<br />' + msg + '<br/>';
				var text =  msg + '<br/>' + place + '<br />' + number + '<br />';
				$("#result").html(text);
			},
			error: function(){
				alert('查询失败，请检查输入');
				$('#idnumber').val('');
			}
		});
	});
	$('#get-cardname').click(function(){
		var idname = $('#idname').val();
		if (idname.length == 0) {
			alert("属地不能为空");
			return;
		}
		var csrf = $(this).data('csrf');
		var url = $(this).data('ajax-url');
		$.ajaxSetup({
			data: {
				'csrfmiddlewaretoken': csrf
			}
		});
		$.ajax({
			type:'post',
			url: url,
			data: {
				'cardname': idname
			},
			dataType: 'json',
			success: function(ret){
				var msg = ret['msg'];
				var text =  msg + '<br/>';
				$.each(ret['cards'], function(i, card){
					var number = card["number"];
					var place = card['place'];
					text = text + place + '<br />' + number + '<br />';
				});
				$("#result").html(text);
			},
			error: function(){
				alert('查询失败，请检查输入');
				$('#idname').val('');
			}
		});
	});
})
/*
	$('#get-cardid').click(function() {
		var idnumber = $('#idnumber').val();
		if (idnumber.length == 0) {
			alert("身份证号不能为空！");
			return;
		}
		var csrf = $(this).data('csrf');
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
				'cardid': idnumber,
			},
			dataType: 'json',
			success: function(ret){
				alert('here');
				var json = eval(ret);
		//alert(json);
				var number = json.number
				var place = json.place;
				//var sex = json.sex;
				//var age = json.age;
				var msg = json.msg;
				//var text = place + '<br />' + sex + '<br />' + msg + '<br/>';
				var text = place + '<br />' + number + '<br />' + msg + '<br/>';
				$("#result").html(text);
			},
			error: function(ret) {
				alert(ret.msg);
			},

		});
	});
})
*/
