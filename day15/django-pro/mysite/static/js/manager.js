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

//全选
function SelectAll(){
    $(".tabletop input:checkbox ").prop("checked",true);
};
function SelectNo(){
    $(".tabletop input:checkbox ").prop("checked",false);
};

//反选
function SelectSide(){
    //isChecked=$(".tabletop input:checkbox ").prop("checked");
    //if (isChecked){
    //    $(".tabletop input:checkbox ").prop("checked",false);
    //}else{
    //    $(".tabletop input:checkbox ").prop("checked",true);
    //}
    $(".tabletop input:checkbox ").each(function(){
        if ($(this).prop("checked")){
            $(this).prop("checked",false);
        }else{
            $(this).prop("checked",true);
        };
    });
};

//编辑模式
function editMode(ths){
    $(ths).css("background-color","red")
    $(".tabletop input:checkbox ").each(function(){
        if ($(this).prop("checked")){
            console.log("checked")
            $(this).siblings().each(function(){
                console.log($(this).text())
                console.log("yes")
                if ($(this).text()){
                    var inner="<input  type='text' value=" + $(this).text() + ">";
                    $(this).text("")
                    $(this).append(inner)
                    console.log("ok")
                }
            })
        }
    })
}

//保存
function Save(ths){
    $(ths).prev().css("background-color","")
};

function addMode(){
    $("#add").removeClass("hide");
    $(".second-side").removeClass("hide");

};

function cancle(){
     $("#add").addClass("hide");
    $(".second-side").addClass("hide");
}


function saveRecord(){
    flag=true;
    $("#add input:text").each(function(){
        if(!$(this).val()){
            $(this).addClass("waring")
            flag =  false;
        }else{
            $(this).removeClass("waring")
        }
    })
    return flag;

}


function cleaning(){
    $("#add input:text").val("");
    $("#add input:text").removeClass("waring")
}