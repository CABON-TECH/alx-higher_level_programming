#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number to a list
 * @head: The head of the list
 * @number: the number to be inserted
 *
 * Return: The address of the inserted number, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *prev = NULL;
	listint_t *new_node;

	if (head == NULL)
		return (NULL);
	node = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	while (node != NULL)
	{
		if (node->n > number)
		{
			if (prev != NULL)
			{
				new_node->next = prev->next;
				prev->next = new_node;
			}
			else
			{
				new_node->next = node;
				*head = new_node;
			}
			return (new_node);
		}
		prev = node;
		node = node->next;
	}
	if (*head == NULL)
		*head = new_node;
	else
	{
		new_node->next = prev->next;
		prev->next = new_node;
	}
	return (new_node);
}
