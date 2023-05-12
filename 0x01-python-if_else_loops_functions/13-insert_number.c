#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: Double pointer to a singly linked list
 *
 * @number: Value of the new node.
 *
 * Return: The address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	int putt = 0;
	listint_t *begins_node = NULL, *normal = NULL, *after = NULL;

	if (head == NULL)
		return (NULL);
	begins_node = malloc(sizeof(listint_t));
	if (!begins_node)
		return (NULL);
	begins_node->n = number, begins_node->next = NULL;
	if (*head == NULL)
	{
		*head = begins_node;
		return (*head);
	}
	normal = *head;
	if (number <= normal->n)
	{
		begins_node->next = normal, *head = begins_node;
		return (*head);
	}
	if (number > normal->n && !normal->next)
	{
		normal->next = begins_node;
		return (begins_node);
	}
	after = normal->next;
	while (normal)
	{
		if (!after)
			normal->next = begins_node, putt = 1;
		else if (after->n == number)
			normal->next = begins_node, begins_node->next = after, putt = 1;
		else if (after->n > number && normal->n < number)
			normal->next = begins_node, begins_node->next = after, putt = 1;
		if (putt)
			break;
		after = after->next, normal = normal->next;
	}
	return (begins_node);
}
