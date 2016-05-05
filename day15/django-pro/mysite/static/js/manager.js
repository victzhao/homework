/**
 * Created by boboer on 2016/5/3.
 */
//进入编辑模式




function doEdit(tag){
    tag.each(function(){
        isEdited = $(this).attr("edit-enable");
        if (isEdited == "true"){
            currentVal=$(this).text();
            temp='<input type="text" value="' + currentVal  + '" />'
            $(this).html(temp);
        };
    });
};

//退出编辑模式
function outEdit(tags){
    tags.each(function(){
        isEdited = $(this).attr("edit-enable");
        if(isEdited=="true"){
            currentVal=$(this).children().val()
            $(this).html(currentVal)
        }
    });
};


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
    if($("#edit").hasClass("editing")){
        $(".tabletop input:checkbox ").each(function(){
            if ($(this).prop("checked")){

            }else{
                $(this).prop("checked",true);
                tags=$(this).parent().siblings();
                doEdit(tags)
            };
        });

    }else{

        $(".tabletop input:checkbox ").prop("checked",true);
    }

};
function SelectNo(){
    if ($("#edit").hasClass("editing")){
        $(".tabletop input:checkbox ").each(function(){
            if ($(this).prop("checked")){
                $(this).prop("checked",false);
                tags=$(this).parent().siblings();
                outEdit(tags);
            }
        })
    }else{
        //直接取消选中
        $(".tabletop input:checkbox ").prop("checked",false);
    }
};

//反选
function SelectSide(){
    if($("#edit").hasClass("editing")){
        //反选并进入编辑模式
        $(".tabletop input:checkbox ").each(function(){
        if ($(this).prop("checked")){
            $(this).prop("checked",false);
            tags=$(this).parent().siblings();
            outEdit(tags);
        }else{
            $(this).prop("checked",true);
            tags=$(this).parent().siblings();
            doEdit(tags)
            };
        });
        //进入编辑模式

    }else{
        //只反选
        $(".tabletop input:checkbox ").each(function(){
        if ($(this).prop("checked")){
            $(this).prop("checked",false);
        }else{
            $(this).prop("checked",true);
            };
        });
    }
};

//编辑模式
function editMode(ths){
    if(!$(ths).hasClass("editing")){
        $(ths).addClass("editing");
        $(".tabletop input:checkbox ").each(function(){
        if ($(this).prop("checked")){
            tags=$(this).parent().siblings();
            doEdit(tags);
        };
    });
    }
};

//保存
function Save(ths){
    if($(ths).prev().hasClass("editing")){
        $(ths).prev().removeClass("editing");
        $(".tabletop input:checkbox ").each(function(){
        if($(this).prop("checked")){
            tags=$(this).parent().siblings();
            outEdit(tags);
            $(this).prop("checked",false)
        }
    })
    }else{
        alert("请进入编辑模式再操作！")
    }
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


function SelectBox(ths){

    if($("#edit").hasClass("editing")){
        tags=$(ths).parent().siblings();
        doEdit(tags);
    };
};

function singleEdit(ths){
    if(!$("#edit").hasClass("editing")){
        $(ths).parent().siblings().first().children().prop("checked",true)
        $("#edit").addClass("editing")
        doEdit($(ths).parent().siblings());
    }
}


function singleDelete(){

}