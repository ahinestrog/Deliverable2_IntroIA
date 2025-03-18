# Inicialización de la base de conocimiento
knowledge_base = [
    "If feber then diagnose posible infection",
    "If cough then diagnose posible flu or respiratory infection",
    "If sore throat then diagnose posible flu or sore infection",
    "If headache then diagnose posible migraine or infection ",
]
t = 0  # Contador de tiempo

# Función para añadir información a la base de conocimiento
def tell(kb, sentence):
    kb.append(sentence)

# Función para realizar consultas a la base de conocimiento
def ask(kb, query):
    # Busca en la base de conocimiento una acción relacionada con la consulta
    for sentence in kb:
        if query in sentence:
            return sentence.split(" then ")[1]
    return None

# Función que convierte la percepción en una oración para añadir a la base de conocimiento
def make_percept_sentence(percept, t):
    return f"At time {t}, perceive {percept}"

# Función que genera una consulta sobre qué acción tomar
def make_action_query(percept):
    return f"If {percept}"

# Función que genera una oración sobre la acción tomada y la añade a la base de conocimiento
def make_action_sentence(action, t):
    return f"At time {t}, take action {action}"

# Función KB-AGENT
def kb_agent(percept, kb, t):
    tell(kb, make_percept_sentence(percept, t))  # Añadir la percepción a la base de conocimiento
    action = ask(kb, make_action_query(percept))  # Consulta sobre qué acción tomar
    if action is None:
        action = "diagnose nothing"  # Si no se encuentra una acción, toma una acción por defecto
    tell(kb, make_action_sentence(action, t))  # Registra la acción tomada
    t += 1  # Incrementa el contador de tiempo
    return action, t

# Ejemplo de uso del agente
perception = "feber"
action, t = kb_agent(perception, knowledge_base, t)
print("Percepción:", perception)
print("Acción tomada:", action)
print("Base de conocimiento actualizada:")
for sentence in knowledge_base:
    print(sentence)

# Otro ejemplo con una percepción diferente
perception = "cough" 
action, t = kb_agent(perception, knowledge_base, t)
print("Percepción:", perception)
print("Acción tomada:", action)
print("Base de conocimiento actualizada:")
for sentence in knowledge_base:
    print(sentence)

# Un tercer ejemplo con una percepción nueva
perception = "Diarrhea"
action, t = kb_agent(perception, knowledge_base, t)
print("Percepción:", perception)
print("Acción tomada:", action)
print("Base de conocimiento actualizada:")
for sentence in knowledge_base:
    print(sentence)