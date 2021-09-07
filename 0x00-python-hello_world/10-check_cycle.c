#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *p1 = list, *p2 = (list)->next;

	while(p1 != p2 && p2 != NULL)
	{
		p1 = p1->next;
		p2 = p2->next;
		if (p2 == NULL)
			return (0);
		p2 = p2->next;
	}
	if (p1 == p2)
		return (1);
	else
		return (0);
}
