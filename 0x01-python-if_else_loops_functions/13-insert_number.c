#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the address of the first node.
 * @number: number to be inserted.
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	if (head == NULL || *head == NULL)
		return (add_nodeint_end(head, number));
	current = *head;
	while (current->next)
	{
		if (current->next->n > number)
			break;
		current = current->next;
	}
	if (current->next == NULL || current == NULL)
		return (add_nodeint_end(head, number));
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = current->next;
	current->next = new;
	return (new);
}
