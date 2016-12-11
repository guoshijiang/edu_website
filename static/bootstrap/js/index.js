$(function(){
	var timu = $(".timu");
	var lis = timu.find("span");
	var timer=null;
	var speed = 1000;
	timu.hover(function()
	{
		clearInterval(timer);
		$(this).children(".array").stop().fadeIn();
	}, function()
	{
		clearInterval(timer);
		timer=setInterval(function()
		{
			move(true);
		},speed)
		$(this).children(".array").stop().fadeOut();
	})
	//核心语句
	var json=[
		{
			zIndex:2
		},{
			zIndex:3
		},{
			zIndex:4
		},{
			zIndex:3
		},{
			zIndex:2
		}];
		move();
		var flag = true;

		$('.qian').on("click", function()
		{
			if(flag == true)
			{
				move(false);
				flag = false;
			}	
		});
		$('.hou').on("click", function()
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
			$("span").each(function(i)
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
