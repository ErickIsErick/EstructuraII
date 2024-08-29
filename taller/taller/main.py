from LinkedList import LinkedList

LinkedList = LinkedList()



print("#### Imprimir números del 1 al 10")
for i in range(1,11):
    LinkedList.insert_at_beginning(i)
LinkedList.mostrar()
print("####\n\n")


print("#### Revertir esa lista")
LinkedList.mostrar()
print("####\n\n")


print("### Eliminar todos los nodos con valor específico")
LinkedList.del_matching_nodes(9)
LinkedList.del_matching_nodes(8)
LinkedList.del_matching_nodes(7)
LinkedList.mostrar()
print("####\n\n")



print("### Encontrar el número más grande dentro de la lista enlazada")
LinkedList.mostrar()
print(f"El número más grande es: {LinkedList.maxElement()}")


print("### El quinto punto no se puede resolver porque los métodos push, pop, enqueue y dequeue no existen ni se pueden implementar para las listas enlazadas, pero sí para las listas nativas simples de Python.")