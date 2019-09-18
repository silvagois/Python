package br.com.crud.dao;

import antlr.collections.List;
import br.com.crud.bean.Pessoa;

public interface PessoaDao {

	public boolean inserePessoa (Pessoa pessoa);
	public boolean alteraPessoa (Pessoa pessoa);
	public boolean excluiPessoa (Pessoa pessoa);
	public Pessoa consultarPessoa (Pessoa pessoa);
	public List listarPessoa();
	
	
	
}
