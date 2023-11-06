#include "lists.h"

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: pointer to pointer to the list.
 *
 * Return: a pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *tmp = NULL, *old = *head;

	if (head == NULL || *head == NULL)
		return (NULL);
	while (*head != NULL)
	{
		*head = (*head)->next;
		old->next = tmp;
		tmp = old;
		old = *head;
	}
	*head = tmp;
	return (*head);
}

/**
 * nodesCtr - count the number of nodes in linked list
 * @head: pointer to the head of the list
 * Return: number of nodes
 */
int nodesCtr(listint_t **head)
{
	int ctr = 0;
	listint_t *cur = *head;

	while (cur != NULL)
	{
		ctr++;
		cur = cur->next;
	}
	return (ctr);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *cur, *first, *last;
	int size, i;

	if (head == NULL || *head == NULL)
		return (PALINDROME);
	size = nodesCtr(head);
	cur = first = *head;
	for (i = 0; i < size / 2; i++)
		cur = cur->next;
	last = reverse_listint(&cur);
	for (i = 0; (i < (size / 2)) && first != NULL && last != NULL; i++)
	{
		if (first->n != last->n)
			return (NOT_PALINDROME);
		first = first->next;
		last = last->next;
	}
	return (PALINDROME);
}
