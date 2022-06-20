from db.database import Graph

class JogoDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://18.234.164.0:7687', user='neo4j', password='tellers-cone-amplifiers')

    def createJogo(self, jogo):
        return self.db.execute_query('CREATE (:Jogo {name:$name, preco:$preco})',
                                     {'name': jogo['name'], 'preco':jogo['preco']})

    def createPlataforma(self, jogo):
        return self.db.execute_query('CREATE (:Plataforma {name:$nomePlataforma})',
                                     {'nomePlataforma': jogo})

    def createDesenvolvedora(self, jogo):
        return self.db.execute_query('CREATE (:Desenvolvedora {name:$nomeDesenvolvedora})',
                                     {'nomeDesenvolvedora': jogo['nomeDesenvolvedora']})

    def createRelacionamentoPlat(self, jogo):
        return self.db.execute_query('MATCH (j:Jogo{name:$name}),(p:Plataforma{name:$nomePlataforma}) CREATE (j)-[:JOGA_EM]->(p)',
                                     {'name': jogo['name'], 'nomePlataforma': jogo['nomePlataforma']})

    def createRelacionamentoDev(self, jogo):
        return self.db.execute_query('MATCH (j:Jogo{name:$name}),(d:Desenvolvedora{name:$nomeDesenvolvedora}) CREATE (d)-[:CRIOU]->(j)',
                                     {'name': jogo['name'], 'nomeDesenvolvedora': jogo['nomeDesenvolvedora']})

    def readJogos(self):
        return self.db.execute_query('MATCH (j:Jogo) RETURN j.name, j.preco')

    def update_preco(self,jogo):
        return self.db.execute_query('MATCH (j:Jogo {name:$name}) SET j.preco = $preco return j',
                                     {'name': jogo['name'], 'preco': jogo['preco']})

    def delete(self, jogo):
        return self.db.execute_query('MATCH (j:Jogo {name:$name}) DETACH DELETE j',
                                     {'name': jogo['name']})

    def deleteTudo(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')

dao = JogoDAO()

dao.db.close()

