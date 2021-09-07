#include "lists.h"

/**
  * check_cycle - checks if there is a cycle in a linked list
  * @list: the list
  * Return: 1 if cycle, 0 if non
  */

int check_cycle(listint_t *list)
{
	listint_t *p1 = list, *p2 = list;

	do {
		p1 = p1->next;
		p2 = p2->next;
		if (p2 == NULL)
			return (0);
		p2 = p2->next;
	} while (p1 != p2 && p2 != NULL);
	if (p1 == p2)
		return (1);
	else
		return (0);
}
