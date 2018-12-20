var dalog;
var dalog2;
var show_yzm = "";
var code = new Array('144031539110','131001570151','133011501118','111001571071');
var code10 = new Array('1440315391','1310015701','1330115011','1110015710');
var oldweb = 0;
var yzmSj = "";
var jmmy = "";
var fplx = "99";
var skxt = 0;
var xsje = 1;
var swjgmc = "";
var delayFlag = "";
var delayTime = 6;
var delayMessage = "";


$(function () {
$("#fpdm").keyup(function () {
    var fpdm = $("#fpdm").val().trim();
    acb(fplx)
});
$('#fpdm').blur(function () {
    var fpdm = $("#fpdm").val().trim();
    if (fpdm.length == 10 || fpdm.length == 12) {
        afcdm(fpdm)
    } else {
        $("#fpdmjy").addClass("tip_common_wrong");
        $("#fpdmjy").addClass("font_red");
        $("#fpdmjy").html("发票代码有误!")
    }
    acb(fplx)
});
$("#fphm").keyup(function () {
    var fphm = $("#fphm").val().trim();
    if (fphm.length >= 8) {
        ahmch(fphm)
    } else {
        $("#fphmjy").removeClass();
        $("#fphmjy").addClass("tip_common");
        $("#fphmjy").html("请输入发票号码")
    }
    acb(fplx)
});
$('#fphm').blur(function () {
    var fphm = $("#fphm").val().trim();
    if (fphm.length != 0 && fphm.length < 8) {
        ahmch(fphm)
    }
    var fpdm = $("#fpdm").val().trim();
    afcdm(fpdm);
    acb(fplx)
});
$("#kjje").keyup(function () {
    var kjje = "";
    var fpdm = $("#fpdm").val().trim();
    var classInfo = $("#kjjejy").attr('class');
    $("#kjjejy").removeClass(classInfo);
    if (fpdm == "" || fplx == "01" || fplx == "02" || fplx == "03" || fplx == "15" || fplx == "99") {
        $("#kjje").attr('maxlength', '20');
        kjje = $("#kjje").val().trim();
        if (!aje(fpdm, kjje)) {
            $("#kjjejy").addClass("tip_common_wrong");
            $("#kjjejy").addClass("font_red");
            if (fplx == "02") {
                $("#kjjejy").html("合计金额有误!")
            } else if (fplx == "03") {
                $("#kjjejy").html("不含税价有误!")
            } else if (fplx == "15") {
                $("#kjjejy").html("车价合计有误!")
            } else {
                $("#kjjejy").html("开票金额有误!")
            }
        } else {
            $("#kjjejy").addClass("tip_common_right");
            $("#kjjejy").html(" ")
        }
    } else if (fplx == "04" || fplx == "10" || fplx == "11" || fplx == "14") {
        $("#kjje").attr('maxlength', '6');
        kjje = $("#kjje").val().trim();
        if (kjje.length >= 6) {
            if (!ajy(kjje)) {
                $("#kjjejy").addClass("tip_common_wrong");
                $("#kjjejy").addClass("font_red");
                $("#kjjejy").html("校验码有误!")
            } else {
                $("#kjjejy").addClass("tip_common_right");
                $("#kjjejy").html(" ")
            }
        } else {
            $("#kjjejy").removeClass();
            $("#kjjejy").addClass("tip_common");
            $("#kjjejy").html("请输入校验码<font color=\"red\" size=\"4\">后六位</font>")
        }
    }
    acb(fplx)
});
$("#kjje").blur(function () {
    var kjje = $("#kjje").val().trim();
    var fpdm = $("#fpdm").val().trim();
    var classInfo = $("#kjjejy").attr('class');
    $("#kjjejy").removeClass(classInfo);
    if (fpdm == "" || fplx == "01" || fplx == "02" || fplx == "03" || fplx == "15" || fplx == "99") {
        if (kjje.length != 0) {
            if (!aje(fpdm, kjje)) {
                $("#kjjejy").addClass("tip_common_wrong");
                $("#kjjejy").addClass("font_red");
                if (fplx == "02") {
                    $("#kjjejy").html("合计金额有误!")
                } else if (fplx == "03") {
                    $("#kjjejy").html("不含税价有误!")
                } else if (fplx == "15") {
                    $("#kjjejy").html("车价合计有误!")
                } else {
                    $("#kjjejy").html("开票金额有误!")
                }
            } else {
                $("#kjjejy").addClass("tip_common_right");
                $("#kjjejy").html(" ")
            }
        } else {
            $("#kjjejy").removeClass();
            $("#kjjejy").addClass("tip_common");
            if (fplx == "02") {
                $("#kjjejy").html("请输入合计金额")
            } else if (fplx == "03") {
                $("#kjjejy").html("请输入不含税价")
            } else if (fplx == "15") {
                $("#kjjejy").html("请输入车价合计")
            } else {
                $("#kjjejy").html("请输入开具金额")
            }
        }
    } else if (fplx == "04" || fplx == "10" || fplx == "11" || fplx == "14") {
        if (kjje.length != 0) {
            if (!ajy(kjje)) {
                $("#kjjejy").addClass("tip_common_wrong");
                $("#kjjejy").addClass("font_red");
                $("#kjjejy").html("校验码有误!")
            } else {
                $("#kjjejy").addClass("tip_common_right");
                $("#kjjejy").html(" ")
            }
        } else {
            $("#kjjejy").removeClass();
            $("#kjjejy").addClass("tip_common");
            $("#kjjejy").html("请输入校验码<font color=\"red\" size=\"4\">后六位</font>")
        }
    }
    acb(fplx)
});
$("#kprq").keyup(function () {
    var kprq = $("#kprq").val().trim();
    if (kprq.length >= 8) {
        kprqChange(kprq)
    } else {
        $("#kprqjy").removeClass();
        $("#kprqjy").addClass("tip_common");
        $("#kprqjy").html("请输入开票日期")
    }
    acb(fplx)
});
$("#kprq").blur(function () {
    var kprq = $("#kprq").val().trim();
    if (kprq == "") {
        $('#kprq').val("YYYYMMDD");
        $('#kprq').css('color', '#999999')
    }
    if (kprq.length != 0) {
        kprqChange(kprq)
    } else {
        $("#kprqjy").removeClass();
        $("#kprqjy").addClass("tip_common");
        $("#kprqjy").html("请输入开票日期")
    }
    acb(fplx)
});
$('#yzm').focus(function () {
    var value = $('#yzm').val();
    var defaultValue = "请输入验证码";
    if (value == defaultValue) {
        $('#yzm').val('');
        $('#yzm').css('color', '#000000')
    }
});
$('#yzm').blur(function () {
    var value = $('#yzm').val();
    if (value == "") {
        $('#yzm').val('请输入验证码');
        $('#yzm').css('color', '#999999')
    }
    acb(fplx)
});
$("#yzm").keyup(function () {
    var yzm = $("#yzm").val().trim();
    var classInfo = $("#yzmjy").attr('class');
    $("#yzmjy").removeClass(classInfo);
    if (!avym(yzm)) {
        $("#yzmjy").addClass("tip_common_wrong");
        $("#yzmjy").addClass("font_red")
    } else {
        $("#yzmjy").html("&nbsp")
    }
    acb(fplx)
});
$("#yzm_img").click(function () {
    var fpdm = $("#fpdm").val().trim();
    var fphm = $("#fphm").val().trim();
    if (fpdm == "" || fphm == "") {
        jAlert('请先输入发票代码及发票号码!', '提示')
    } else {
        if (ckdm(fpdm) && ahm(fphm)) {
            getYzmXx()
        } else {
            jAlert('请输入正确发票代码及发票号码!', '提示')
        }
    }
});
$('#reset').click(function () {
    arw()
});

function ckdm(fpdm) {
    if (fpdm.length == 10 || fpdm.length == 12) {
        var c = /^[0-9]*$/;
        var f = c.test(fpdm);
        if (f == false) {
            return false
        } else {
            var swjginfo = getSwjg(fpdm, 0);
            if (swjginfo.length == 0) {
                return false
            } else {
                if (!adm(fpdm) || swjginfo.length == 0) {
                    return false
                } else {
                    return true
                }
            }
        }
    } else {
        return false
    }
}
});