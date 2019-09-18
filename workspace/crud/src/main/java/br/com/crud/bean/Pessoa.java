package br.com.crud.bean;

import java.io.Serializable;
import java.util.Calendar;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.SequenceGenerator;
import javax.persistence.Table;

@Entity
@Table(name = "Pessoa")
@SequenceGenerator(name = "hibernate_sequence_pessoa", sequenceName = "hibernate_sequence_pessoa", allocationSize = 1)
public class Pessoa implements Serializable {

	private static final long serialVersionUID = 1L;
	@Id
	@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "hibernate_sequence_pessoa")
	@Column(name = "idPessoa")
	private Long idPessoa;
	
	@Column(name = "nomePessoa")
	private String nomePessoa;
	
	@Column(name = "emailPessoa")
	private String emailPessoa;
	
	@Column(name = "dataNascimento")
	private Calendar dataNascimento;
	
	@Column(name = "generoPessoa")
	private String generoPessoa;

	public Long getIdPessoa() {
		return idPessoa;
	}

	public void setIdPessoa(Long idPessoa) {
		this.idPessoa = idPessoa;
	}

	public String getNomePessoa() {
		return nomePessoa;
	}

	public void setNomePessoa(String nomePessoa) {
		this.nomePessoa = nomePessoa;
	}

	public String getEmailPessoa() {
		return emailPessoa;
	}

	public void setEmailPessoa(String emailPessoa) {
		this.emailPessoa = emailPessoa;
	}

	
	public Calendar getDataNascimento() {
		return dataNascimento;
	}

	public void setDataNascimento(Calendar dataNascimento) {
		this.dataNascimento = dataNascimento;
	}

	public String getGeneroPessoa() {
		return generoPessoa;
	}

	public void setGeneroPessoa(String generoPessoa) {
		this.generoPessoa = generoPessoa;
	}

	public static long getSerialversionuid() {
		return serialVersionUID;
	}
	
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((dataNascimento == null) ? 0 : dataNascimento.hashCode());
		result = prime * result + ((emailPessoa == null) ? 0 : emailPessoa.hashCode());
		result = prime * result + ((generoPessoa == null) ? 0 : generoPessoa.hashCode());
		result = prime * result + ((idPessoa == null) ? 0 : idPessoa.hashCode());
		result = prime * result + ((nomePessoa == null) ? 0 : nomePessoa.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Pessoa other = (Pessoa) obj;
		if (dataNascimento == null) {
			if (other.dataNascimento != null)
				return false;
		} else if (!dataNascimento.equals(other.dataNascimento))
			return false;
		if (emailPessoa == null) {
			if (other.emailPessoa != null)
				return false;
		} else if (!emailPessoa.equals(other.emailPessoa))
			return false;
		if (generoPessoa == null) {
			if (other.generoPessoa != null)
				return false;
		} else if (!generoPessoa.equals(other.generoPessoa))
			return false;
		if (idPessoa == null) {
			if (other.idPessoa != null)
				return false;
		} else if (!idPessoa.equals(other.idPessoa))
			return false;
		if (nomePessoa == null) {
			if (other.nomePessoa != null)
				return false;
		} else if (!nomePessoa.equals(other.nomePessoa))
			return false;
		return true;
	}


}
