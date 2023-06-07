#include "lists.h"
/**
 * insert_node - inserts node
 * @head: addr of head
 * @number: number
 * Return: pointer to head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *ptr;

	ptr = malloc(sizeof(listint_t));
	ptr->n = number;
	ptr->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		ptr->next = *head;
		*head = ptr;
		return (*head);
	}
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	ptr->next = current->next;
	current->next = ptr;
	return (*head);
}
