#include "lists.h"
/**
 * check_cycle - checks for cycle
 * @list: linkedlist
 * Return: 0 if no cycle and 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while(fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);

	}
	return (0);
}
