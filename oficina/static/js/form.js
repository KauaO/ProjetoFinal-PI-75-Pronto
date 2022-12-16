const form = document.getElementById("form");
const largura = document.getElementById("txtlargura");
const perfil = document.getElementById("txtperfil");
const tamanho = document.getElementById("txttamanho");
const marca = document.getElementById("txtmarca");
const tipo = document.getElementById("txttipo");
const material = document.getElementById("txtmaterial");
const cor = document.getElementById("txtcor");
const valor = document.getElementById("txtvalor");
const quantidade = document.getElementById("txtquantidade");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  checkInputs();
});

function checkInputs() {
  const larguraValue = largura.value;
  const perfilValue = perfil.value;
  const tamanhoValue = tamanho.value;
  const marcaValue = marca.value;
  const tipoValue = tipo.value;
  const materialValue = material.value;
  const corValue = cor.value;
  const valorValue = valor.value;
  const quantidadeValue = quantidade.value;

  if (valorValue == "") {
    setErrorFor(valor, "O campo valor é obrigatório.");
    console.log("----aqui");
  } else {
    setSuccessFor(valor);
  }
  if (perfilValue == "") {
    setErrorFor(perfil, "O campo perfil é obrigatório.");
  } else {
    setSuccessFor(perfil);
  }
}

function setErrorFor(input, message) {
  const formControl = input.parentElement;
  const small = formControl.querySelector("small");

  small.innerText = message; //adiciona mensagem de erro

  formControl.className = "form-control error";
}

function setSuccessFor(input) {
  const formControl = input.parentElement; //retorna a div do input

  formControl.className = "form-control success";
}
