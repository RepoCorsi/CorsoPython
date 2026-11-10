def doppio(x):
    """
    fa il doppio
    devi passare un solo numero
    """
    
    return x*2

def esegui_tante_volte(quanto):
    if quanto>0: #condizione di uscita per terminare l'esecuzione
        
        print("sto chiamando me stessa",quanto,"volte")
    
        quanto-=1 #tolgo 1 ogni volta che chiamo la funzione
        esegui_tante_volte(quanto)

def crea_sandwich(tipo_pane,*ingredienti,**opzioni):
    print("panino con pane di tipo",tipo_pane)
    if ingredienti:
        print("hai scelto questi ingredienti:")
        print(f"{",".join(ingredienti)}") #lista ingredienti passata alla funzione
    if opzioni:
        print("hai scelto queste opzioni:")
        for chiave, valore in opzioni.items():
            print(f"- > {chiave}:{valore}")

