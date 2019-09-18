package br.com.crud.DaoImpl;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.Transaction;

import antlr.collections.List;
import br.com.crud.bean.Pessoa;
import br.com.crud.dao.PessoaDao;
import br.com.crud.util.HibernateUtil;

public class PessoaDaoImpl implements PessoaDao {

	private Session session = null;
	private Transaction transaction = null;

	public boolean inserePessoa(Pessoa pessoa) {
		boolean retorno = false;
		try {
			session = HibernateUtil.getSessionFactory().openSession();
			transaction = session.beginTransaction();
			System.out.println("DAo- NOME:" + pessoa.getNomePessoa());
			session.persist(pessoa);
			transaction.commit();
			retorno = true;

		} catch (HibernateException e) {
			transaction.rollback();
			e.printStackTrace();
		} finally {
			session.close();
		}
		return retorno;
	}

	public boolean alteraPessoa(Pessoa pessoa) {
		boolean retorno = false;
		try {
			session = HibernateUtil.getSessionFactory().openSession();
			transaction = session.beginTransaction();
			session.update(pessoa);
			transaction.commit();
			retorno = true;
		} catch (HibernateException e) {
			transaction.rollback();
			e.printStackTrace();
		} finally {
			session.close();
		}
		return retorno;
	}

	public boolean excluiPessoa(Pessoa pessoa) {
		boolean retorno = false;
		try {
			session = HibernateUtil.getSessionFactory().openSession();
			transaction = session.beginTransaction();
			session.delete(session.get(Pessoa.class, pessoa.getIdPessoa()));
			transaction.commit();
			retorno = true;
		} catch (HibernateException e) {
			transaction.rollback();
			e.printStackTrace();
		} finally {
			session.close();
		}
		return retorno;
	}

	public Pessoa consultarPessoa(Pessoa pessoa) {
		Pessoa l = null;
		try {
			session = HibernateUtil.getSessionFactory().openSession();
			l = (Pessoa) session.get(Pessoa.class, pessoa.getIdPessoa());
		} catch (HibernateException e) {
			e.printStackTrace();
		} finally {
			session.close();
		}
		return l;
	}

	public List listarPessoa() {
		List list = null;
		try {
			session = HibernateUtil.getSessionFactory().openSession();
			// aqui pode ocorrer um problema por causa do cast LIST
			list = (List) session.createQuery("select l from Pessoa l").list();
		} catch (HibernateException e) {
			e.printStackTrace();
		} finally {
			session.close();
		}
		return list;

	}

}
