//（一）先让图片轮换起来
//获取id=dd_scroll图片对象
var imgObj = document.getElementById("dd_scroll");
var num = 1;//当前图片、全局变量
var timer2 = window.setInterval("imgSwap()",1000);
function imgSwap()
{
	//修改imgObj的src属性的值
	imgObj.src = "images/dd_scroll_"+num+".jpg";
	//更改序号背景色
	changeBgColor();
	//如果num=7，则num=1
	num++;
	if(num==7)
	{
		num = 1;
	}
}
//给图片增加onMouseOver事件、onMouseOut事件
imgObj.onmouseover = function(){
							window.clearInterval(timer2);
						}
imgObj.onmouseout = function(){
							timer2 = window.setInterval("imgSwap()",1000);
						}

//（二）让序号的背景色，跟着当前图片走。
function changeBgColor()
{
	//获取id=scroll_number的div对象
	var divObj = document.getElementById("scroll_number");
	//获取所有的<li>标签构成的对象数组
	var arr_lis = divObj.getElementsByTagName("li");
	//循环将所有的<li>标签的背景色清空
	for(var i=0;i<arr_lis.length;i++)
	{
		arr_lis[i].style.backgroundColor = "";
	}
	//将当前图片序号，更改背景色为orange
	arr_lis[num-1].style.backgroundColor = "orange";
}
//（三）鼠标放到序号上时，动画停止，图片要切换到相对应的图片上，
//鼠标移开，动画继续
function scrollStop(index)
{
	//清除定时器
	window.clearInterval(timer2);
	//将当前图片序号换成index
	num = index;
	//重新更改图片的src属性的值
	imgObj.src = "images/dd_scroll_"+num+".jpg";
	//更改当前li序号的背景色
	changeBgColor();
}
//鼠标移开，动画继续
function scrollStart()
{
	timer2 = window.setInterval("imgSwap()",1000);
}