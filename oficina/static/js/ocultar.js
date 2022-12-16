$("#select").change(function () {
  var value = $("#select option:selected").text();
  var largura = document.getElementById("largura");
  var perfil = document.getElementById("perfil");
  var tamanho = document.getElementById("tamanho");
  var marca = document.getElementById("marca");
  var tipo = document.getElementById("tipo");
  var material = document.getElementById("material");
  var cor = document.getElementById("cor");
  var btn = document.getElementById("btn");
  var quant = document.getElementById("quant");
  var valor = document.getElementById("val");
  var img = document.getElementById("img");

  console.log(value);
  $(largura).hide();
  $(tipo).hide();
  $(perfil).hide();
  $(tamanho).hide();
  $(material).hide();
  $(cor).hide();
  $(btn).hide();
  $(quant).hide();
  $(val).hide();
  $(img).hide();

  if (value === "pneu") {
    console.log("Mizera dos inferno");
    $(largura).show();
    $(perfil).show();
    $(tamanho).show();
    $(btn).show();
    $(quant).show();
    $(val).show();
    $(img).show();
  }

  if (value === "aro") {
    $(largura).show();
    $(perfil).show();
    $(tamanho).show();
    $(material).show();
    $(cor).show();
    $(btn).show();
    $(quant).show();
    $(val).show();
    $(img).show();
  }

  if (value === "raio") {
    $(largura).show();
    $(perfil).show();
    $(tamanho).show();
    $(tipo).show();
    $(material).show();
    $(cor).show();
    $(btn).show();
    $(quant).show();
    $(val).show();
    $(img).show();
  }

  if (value === "farol") {
    $(tamanho).show();
    $(tipo).show();
    $(material).hide();
    $(btn).show();
    $(quant).show();
    $(val).show();
    $(img).show();
  }
  if (value === "retrovisor") {
    $(tamanho).show();
    $(tipo).show();
    $(material).show();
    $(cor).show();
    $(btn).show();
    $(quant).show();
    $(val).show();
    $(img).show();
  }
});
