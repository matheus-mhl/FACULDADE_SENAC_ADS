class Material {
    codMaterial;
    descMaterial;
    qtdeEstoque;
    cadastrar(codMaterial, descMaterial) {
        this.codMaterial = codMaterial;
        this.descMaterial = descMaterial;
        this.qtdeEstoque = 0;
        sessionStorage.setItem("codMaterial", this.codMaterial);
        sessionStorage.setItem("descMaterial", this.descMaterial);
        sessionStorage.setItem("qtdeEstoque", this.qtdeEstoque);
    }
    obterDados() {
        this.codMaterial = Number(sessionStorage.getItem("codMaterial"));
        this.descMaterial = sessionStorage.getItem("descMaterial");
        this.qtdeEstoque = Number(sessionStorage.getItem("qtdeEstoque"));
    }
    entrarMaterial(valor) {
        this.obterDados();
        this.qtdeEstoque = this.qtdeEstoque + valor;
        sessionStorage.setItem("qtdeEstoque", this.qtdeEstoque);
    }
    sairMaterial(valor) {
        this.obterDados();
        let novoqtdeEstoque = this.qtdeEstoque - valor;
        if (novoqtdeEstoque < 0) {
            return false;
        }
        this.qtdeEstoque = novoqtdeEstoque;
        sessionStorage.setItem("qtdeEstoque", this.qtdeEstoque);
        return true;
    }
}