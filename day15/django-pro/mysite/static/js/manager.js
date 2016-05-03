/**
 * Created by boboer on 2016/5/3.
 */
//为每个菜单绑定事件并执行相应的动作
$(function(){
    $(".left ul").children().each(function(){
        $(this).click(function(){
            $(this).addClass("active")
            $(this).siblings().removeClass("active")
        });
    });
});
