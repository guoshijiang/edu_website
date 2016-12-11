//旋转木马
$(function(){
	var slide = $(".slide");
	var lis = slide.find("li");
	var timer=null;
	var speed = 1000;
	slide.hover(function()
	{
		clearInterval(timer);
		$(this).children(".arrow").stop().fadeIn();
	}, function()
	{
		clearInterval(timer);
		timer=setInterval(function()
		{
			move(true);
		},speed)
		$(this).children(".arrow").stop().fadeOut();
	})
	
	//核心语句
	var json=[
		{
			width:400,
			top:20,
			left:50,
			opacity:0.2,
			zIndex:2
		},{
			width:600,
			top:70,
			left:0,
			opacity:0.8,
			zIndex:3
		},{
			width:800,
			top:100,
			left:200,
			opacity:1,
			zIndex:4
		},{
			width:600,
			top:70,
			left:600,
			opacity:0.8,
			zIndex:3
		},{
			width:400,
			top:20,
			left:750,
			opacity:0.2,
			zIndex:2
		}];
		move();
		var flag = true;
		$('.prev').on("click", function()
		{
			if(flag == true)
			{
				move(false);
				flag = false;
			}	
		});

		$('.next').on("click", function()
		{
			if(flag == true)
			{
				move(true);
				flag = false;
			}	
		})
		
		function move(obj)
		{
			if(obj)
			{
				json.unshift(json.pop());		
			}
			else
			{
				json.push(json.shift());
			}
			/*
			 $.each(json,function(i, value)
			 {
				 lis.eq(i).css("zIndex", json[i].z).end().animate(json, i, function()
				 {
						flag=true;
				 });
			 })
			*/
			$("li").each(function(i)
			{
				$(this).animate(json[i],400, function()
				{
					flag =true;
				});
			})			
		}
		//定时器开始
		timer=setInterval (function()
		{
			move(true);
		}, speed);
})
//旋转木马