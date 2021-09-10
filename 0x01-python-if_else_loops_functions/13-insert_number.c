#include "lists.h"

/**
  * insert_node - inserts a new node in a sorted linked list
  * @head: head pointer
  * @number: data of the new node
  * Return: pointer to new node
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *previous;
	listint_t *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
    new->n = number;

	if (*head == NULL)
	{
		*head = new;
		(*head)->next = NULL;
		return (*head);
	}

	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	new->next = current;
	previous->next = new;
	return (new);
}
